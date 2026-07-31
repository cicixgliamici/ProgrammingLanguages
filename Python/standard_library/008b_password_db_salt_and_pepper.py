"""
Educational example (Part B): Password DB with Salt+Pepper + Login Rate Limiting + Lockout.

Adds on top of the basic Salt+Pepper example:
1) Rate limiting: prevent brute-force by limiting attempts per time window.
2) Temporary lockout: after too many failed attempts, lock account for a while.
3) Notes on how you'd do this with Redis + TTL in a distributed system.

Important:
- Still educational and simplified.
- Real systems also need: MFA, secure password reset, auditing, monitoring,
  IP reputation, device fingerprinting, bot detection, etc.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import os
import secrets
import time
from typing import Final


# =============================================================================
# Pepper (server secret): read from env (good habit)
# =============================================================================
PEPPER: Final[str] = os.getenv("APP_PEPPER", "DEV_ONLY__replace_me_in_env")


# =============================================================================
# Data model (DB row)
# =============================================================================

@dataclass(slots=True)
class UserRecord:
    username: str
    salt_hex: str
    password_hash_hex: str
    iterations: int


# =============================================================================
# Auth DB (PBKDF2 + salt + pepper)
# =============================================================================

class SimpleAuthDB:
    def __init__(self, *, iterations: int = 200_000):
        if iterations < 50_000:
            raise ValueError("iterations too low for a realistic demo")
        self._iterations = iterations
        self.users: dict[str, UserRecord] = {}

    @staticmethod
    def _derive_key(password: str, salt_hex: str, iterations: int) -> str:
        salt = bytes.fromhex(salt_hex)
        material = f"{password}:{PEPPER}".encode("utf-8")
        dk = hashlib.pbkdf2_hmac("sha256", material, salt, iterations, dklen=32)
        return dk.hex()

    def register_user(self, username: str, plain_password: str) -> None:
        if not username:
            raise ValueError("username cannot be empty")
        if username in self.users:
            raise ValueError("username already exists")
        if len(plain_password) < 8:
            raise ValueError("password too short (min 8 for this demo)")

        salt_hex = secrets.token_hex(16)
        pwd_hash_hex = self._derive_key(plain_password, salt_hex, self._iterations)
        self.users[username] = UserRecord(username, salt_hex, pwd_hash_hex, self._iterations)

    def verify_password(self, username: str, candidate_password: str) -> bool:
        """
        Pure password verification (no rate limiting / lockout here).
        Returns False for unknown users.
        """
        user = self.users.get(username)
        if user is None:
            return False
        candidate_hash = self._derive_key(candidate_password, user.salt_hex, user.iterations)
        return hmac.compare_digest(candidate_hash, user.password_hash_hex)


# =============================================================================
# Rate limiting + lockout layer (in-memory)
# =============================================================================
"""
We separate concerns:
- AuthDB verifies passwords
- Security layer enforces rate limits / lockouts

This separation mirrors real architectures:
- auth service/library
- security middleware / gateway / API layer
"""

@dataclass(slots=True)
class AttemptState:
    """
    Tracks recent attempts for one key (e.g., username or (username, IP)).

    - window_start: start timestamp for the current window
    - attempts_in_window: total attempts counted in that window
    - consecutive_failures: how many fails in a row
    - locked_until: timestamp until which login is blocked
    """
    window_start: float
    attempts_in_window: int
    consecutive_failures: int
    locked_until: float


class LoginProtector:
    """
    Simple in-memory protector.

    Parameters:
    - max_attempts_per_window: e.g., 5 attempts
    - window_seconds: e.g., per 60 seconds
    - lockout_after_failures: e.g., 3 consecutive failures
    - lockout_seconds: e.g., lock for 30 seconds

    Keying strategy:
    - simplest: per username
    - better: per (username, IP)
    - best: combine signals (username, IP, device)
    """

    def __init__(
        self,
        *,
        max_attempts_per_window: int = 5,
        window_seconds: float = 60.0,
        lockout_after_failures: int = 3,
        lockout_seconds: float = 30.0,
    ):
        if max_attempts_per_window <= 0:
            raise ValueError("max_attempts_per_window must be positive")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be positive")
        if lockout_after_failures <= 0:
            raise ValueError("lockout_after_failures must be positive")
        if lockout_seconds <= 0:
            raise ValueError("lockout_seconds must be positive")

        self.max_attempts_per_window = max_attempts_per_window
        self.window_seconds = window_seconds
        self.lockout_after_failures = lockout_after_failures
        self.lockout_seconds = lockout_seconds

        self._state: dict[str, AttemptState] = {}

    def _get_state(self, key: str, now: float) -> AttemptState:
        st = self._state.get(key)
        if st is None:
            st = AttemptState(
                window_start=now,
                attempts_in_window=0,
                consecutive_failures=0,
                locked_until=0.0,
            )
            self._state[key] = st
        return st

    def _reset_window_if_needed(self, st: AttemptState, now: float) -> None:
        if now - st.window_start >= self.window_seconds:
            st.window_start = now
            st.attempts_in_window = 0

    def can_attempt(self, key: str) -> tuple[bool, str]:
        """
        Check if a login attempt is allowed at this time.
        Returns (allowed, reason).
        """
        now = time.monotonic()
        st = self._get_state(key, now)

        if now < st.locked_until:
            remaining = st.locked_until - now
            return False, f"LOCKED (try again in {remaining:.1f}s)"

        self._reset_window_if_needed(st, now)

        if st.attempts_in_window >= self.max_attempts_per_window:
            wait = (st.window_start + self.window_seconds) - now
            return False, f"RATE_LIMITED (wait {wait:.1f}s)"

        return True, "OK"

    def record_attempt(self, key: str, success: bool) -> None:
        """
        Update state after an attempt.
        """
        now = time.monotonic()
        st = self._get_state(key, now)

        # if window expired, reset attempts counter
        self._reset_window_if_needed(st, now)

        st.attempts_in_window += 1

        if success:
            # reset consecutive failure counter on success
            st.consecutive_failures = 0
            return

        # failure case
        st.consecutive_failures += 1
        if st.consecutive_failures >= self.lockout_after_failures:
            st.locked_until = now + self.lockout_seconds
            st.consecutive_failures = 0  # reset after applying lockout


# =============================================================================
# Composition: Protected login flow
# =============================================================================

class ProtectedAuthService:
    """
    Combines:
    - password verification (SimpleAuthDB)
    - rate limiting + lockout (LoginProtector)

    This is composition ("has-a"): no inheritance needed.
    """

    def __init__(self, db: SimpleAuthDB, protector: LoginProtector):
        self.db = db
        self.protector = protector

    def login(self, username: str, password: str, *, client_ip: str | None = None) -> tuple[bool, str]:
        """
        Attempt login. Returns (success, message).

        Keying:
        - We'll key by username for simplicity.
        - You can key by f"{username}:{client_ip}" to reduce targeted attacks.
        """
        key = username if client_ip is None else f"{username}:{client_ip}"

        allowed, reason = self.protector.can_attempt(key)
        if not allowed:
            return False, reason

        ok = self.db.verify_password(username, password)

        # Important: record attempt outcome regardless of ok
        self.protector.record_attempt(key, success=ok)

        if ok:
            return True, "LOGIN_OK"
        return False, "INVALID_CREDENTIALS"


# =============================================================================
# Distributed notes (Redis sketch, no code)
# =============================================================================
"""
How to do this in a distributed system (idea sketch):

You don't want rate limit / lockout counters only in memory if you run multiple instances.
A common approach: Redis with TTL and atomic operations.

Example keys:
- rl:{username}:{ip} -> attempt_count with EXPIRE window_seconds
- lf:{username}:{ip} -> consecutive_failures with EXPIRE maybe longer
- lock:{username}:{ip} -> lock flag with TTL = lockout_seconds

You need atomicity to avoid race conditions under high concurrency:
- Use Redis Lua script to:
  1) check lock key
  2) increment attempt count (INCR) and set TTL if first increment
  3) if invalid credentials -> increment failure count and maybe set lock key with TTL
  4) return allow/deny decision

Also: be careful with user enumeration (don’t leak whether user exists).
"""


# =============================================================================
# Demo
# =============================================================================

def main() -> None:
    db = SimpleAuthDB()
    db.register_user("alice", "SuperSecret123")

    protector = LoginProtector(
        max_attempts_per_window=5,
        window_seconds=10.0,
        lockout_after_failures=3,
        lockout_seconds=5.0,
    )

    service = ProtectedAuthService(db, protector)

    print("=== Wrong password attempts (should lock after 3 fails) ===")
    for i in range(4):
        ok, msg = service.login("alice", "wrong-pass")
        print(f"attempt {i+1}: {ok=} {msg=}")

    print("\n=== Immediately try correct password (may be LOCKED) ===")
    ok, msg = service.login("alice", "SuperSecret123")
    print(f"correct password: {ok=} {msg=}")

    print("\nSleeping 5.5s to pass lockout...")
    time.sleep(5.5)

    print("=== Try correct password again ===")
    ok, msg = service.login("alice", "SuperSecret123")
    print(f"after lockout: {ok=} {msg=}")

    print("\n=== Rate limit demo (many attempts quickly) ===")
    for i in range(7):
        ok, msg = service.login("alice", "wrong-pass")
        print(f"burst attempt {i+1}: {ok=} {msg=}")


if __name__ == "__main__":
    main()
