"""
Educational example: simple password database with Salt + Pepper.

Goal:
- Explain how to store passwords safely (for study purposes).
- Show the difference between:
  1) Salt  -> random per-user value stored with the hash.
  2) Pepper -> secret server-side value NOT stored in the database.

Important:
- This file is didactic and intentionally compact.
- Real systems should also include: secure secret management (HSM/KMS),
  account lockouts, audit logs, MFA, password reset flows, etc.
"""

from dataclasses import dataclass
import hashlib
import hmac
import secrets


# ---------------------------------------------------------------------
# In real applications, PEPPER must come from environment/secret manager,
# not hardcoded in source code.
# ---------------------------------------------------------------------
PEPPER = "replace-with-env-secret-in-real-app"


@dataclass
class UserRecord:
    """Represents one user row in our in-memory database."""

    username: str
    salt_hex: str
    password_hash_hex: str


class SimpleAuthDB:
    """
    Very small in-memory auth DB for learning.

    Data model:
    - key: username
    - value: UserRecord(username, salt, hash)

    Security approach used here:
    - hash = SHA-256(salt + password + pepper)
    - salt is unique per user (stored in DB)
    - pepper is secret shared by the server (not in DB)
    """

    def __init__(self):
        self.users: dict[str, UserRecord] = {}

    @staticmethod
    def _hash_password(password: str, salt_hex: str) -> str:
        """
        Compute password hash using salt + password + pepper.

        Why this order isn't critical for concept:
        - The key point is combining all three components consistently.
        """
        material = f"{salt_hex}:{password}:{PEPPER}".encode("utf-8")
        return hashlib.sha256(material).hexdigest()

    def register_user(self, username: str, plain_password: str) -> None:
        """Create a user with random salt and stored hash."""
        if username in self.users:
            raise ValueError("Username already exists")

        # Generate 16 random bytes and store as hex string.
        salt_hex = secrets.token_hex(16)
        password_hash_hex = self._hash_password(plain_password, salt_hex)

        self.users[username] = UserRecord(
            username=username,
            salt_hex=salt_hex,
            password_hash_hex=password_hash_hex,
        )

    def verify_login(self, username: str, candidate_password: str) -> bool:
        """
        Verify login attempt.

        We use hmac.compare_digest to reduce timing-attack leakage.
        """
        user = self.users.get(username)
        if user is None:
            return False

        candidate_hash_hex = self._hash_password(candidate_password, user.salt_hex)
        return hmac.compare_digest(candidate_hash_hex, user.password_hash_hex)


if __name__ == "__main__":
    # -----------------------------------------------------------------
    # Demo flow
    # -----------------------------------------------------------------
    db = SimpleAuthDB()

    db.register_user("alice", "SuperSecret123")

    print("Stored DB row for alice (notice: no plain password):")
    print(db.users["alice"])

    print("\nLogin attempts:")
    print("alice / wrong-pass ->", db.verify_login("alice", "wrong-pass"))
    print("alice / SuperSecret123 ->", db.verify_login("alice", "SuperSecret123"))

    print("\nStudy notes:")
    print("- Salt makes identical passwords produce different hashes per user.")
    print("- Pepper protects users even if DB leaks but server secret does not.")
    print("- Never store plain-text passwords.")