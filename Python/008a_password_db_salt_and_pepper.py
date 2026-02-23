"""
Educational example: simple password database with Salt + Pepper (safer version).

Goal:
- Explain how to store passwords safely (study purposes).
- Show the difference between:
  1) Salt   -> random per-user value stored with the hash
  2) Pepper -> secret server-side value NOT stored in the database
- Show a more realistic approach than plain SHA-256:
  use a password hashing function (PBKDF2) + constant-time compare.

Important:
- Still educational and simplified.
- Real systems also need: secret management (KMS/HSM), lockouts, MFA,
  password reset flows, auditing, monitoring, rate-limiting, etc.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import os
import secrets
from typing import Final


# =============================================================================
# 0) Pepper (server secret): NEVER store in DB, NEVER hardcode in real apps
# =============================================================================
"""
In real apps, pepper should come from:
- environment variables
- a secret manager (AWS/GCP/Azure)
- KMS/HSM

Here we read from env as a better habit than hardcoding.
Set it like:
  export APP_PEPPER="some-long-random-secret"
"""
PEPPER: Final[str] = os.getenv("APP_PEPPER", "DEV_ONLY__replace_me_in_env")


# =============================================================================
# 1) Data model: what's stored in the "database"
# =============================================================================

@dataclass(slots=True)
class UserRecord:
    """
    Represents a user row in our (in-memory) database.

    Stored fields:
    - username
    - salt (hex)
    - password_hash (hex)
    - parameters (iterations) needed to verify later

    Note:
    - We never store the plain password.
    - Salt is NOT secret; pepper IS secret.
    """

    username: str
    salt_hex: str
    password_hash_hex: str
    iterations: int


# =============================================================================
# 2) Auth DB: register + verify
# =============================================================================

class SimpleAuthDB:
    """
    Very small in-memory auth DB for learning.

    Security approach used here:
    - password_hash = PBKDF2-HMAC-SHA256(password + pepper, salt, iterations)
    - salt: random per user, stored in DB
    - pepper: server secret, never stored in DB

    Why PBKDF2 instead of raw SHA-256?
    - Raw hashes are too fast -> attackers can brute-force quickly.
    - PBKDF2 is intentionally slower (key stretching).
    - In modern production, Argon2 or scrypt are often preferred,
      but PBKDF2 is in the Python standard library (good for educational code).
    """

    def __init__(self, *, iterations: int = 200_000):
        if iterations < 50_000:
            # Keep the demo safe-ish; real values depend on hardware and policy.
            raise ValueError("iterations too low for a realistic demo")
        self._iterations = iterations
        self.users: dict[str, UserRecord] = {}

    @staticmethod
    def _derive_key(password: str, salt_hex: str, iterations: int) -> str:
        """
        Derive a password key using PBKDF2-HMAC-SHA256.

        Input material:
        - password + pepper (pepper acts like a global secret)
        - salt (unique per user)

        Output:
        - hex string (DB-friendly)
        """
        salt = bytes.fromhex(salt_hex)

        # Combine password and pepper consistently.
        # (We add a separator to reduce accidental ambiguity.)
        material = f"{password}:{PEPPER}".encode("utf-8")

        dk = hashlib.pbkdf2_hmac(
            "sha256",
            material,
            salt,
            iterations,
            dklen=32,  # 32 bytes = 256-bit derived key
        )
        return dk.hex()

    def register_user(self, username: str, plain_password: str) -> None:
        """Create a user with random salt and stored hash."""
        if not username:
            raise ValueError("username cannot be empty")
        if username in self.users:
            raise ValueError("username already exists")
        if len(plain_password) < 8:
            raise ValueError("password too short (min 8 for this demo)")

        # 16 random bytes (128-bit) of salt is common.
        salt_hex = secrets.token_hex(16)
        pwd_hash_hex = self._derive_key(plain_password, salt_hex, self._iterations)

        self.users[username] = UserRecord(
            username=username,
            salt_hex=salt_hex,
            password_hash_hex=pwd_hash_hex,
            iterations=self._iterations,
        )

    def verify_login(self, username: str, candidate_password: str) -> bool:
        """
        Verify a login attempt.

        Security note:
        - Use constant-time comparison to reduce timing leaks.
        - Return False for unknown users (avoid leaking existence through errors).
        """
        user = self.users.get(username)
        if user is None:
            return False

        candidate_hash_hex = self._derive_key(candidate_password, user.salt_hex, user.iterations)
        return hmac.compare_digest(candidate_hash_hex, user.password_hash_hex)


# =============================================================================
# 3) Quick notes (salt vs pepper, and common pitfalls)
# =============================================================================
"""
Salt:
- Random per user.
- Stored in DB next to the hash.
- Prevents "same password -> same hash" across users.
- Defeats many precomputed attacks (rainbow tables).

Pepper:
- Secret shared by the server/app.
- Not stored in the DB.
- If DB leaks but pepper does NOT, brute-forcing becomes much harder.

Pitfalls:
- Never store plain-text passwords.
- Avoid fast hashes (SHA-256) for passwords; use slow KDFs (PBKDF2/scrypt/Argon2).
- Use constant-time compare for hashes.
- Protect pepper with real secret management in production.
"""


# =============================================================================
# Demo
# =============================================================================

def main() -> None:
    db = SimpleAuthDB(iterations=200_000)

    db.register_user("alice", "SuperSecret123")
    db.register_user("bob", "SuperSecret123")  # same password, different salt -> different hash

    print("Stored DB row for alice (notice: no plain password):")
    print(db.users["alice"])

    print("\nStored DB row for bob (same password, but different salt/hash):")
    print(db.users["bob"])

    print("\nLogin attempts:")
    print("alice / wrong-pass ->", db.verify_login("alice", "wrong-pass"))
    print("alice / SuperSecret123 ->", db.verify_login("alice", "SuperSecret123"))

    print("\nStudy notes:")
    print("- Salt makes identical passwords produce different hashes per user.")
    print("- Pepper helps even if DB leaks but server secret does not.")
    print("- PBKDF2 slows brute-force compared to raw SHA-256.")


if __name__ == "__main__":
    main()
