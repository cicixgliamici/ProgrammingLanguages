"""
System Design (Python sketch): Token Bucket Rate Limiter.

Educational goals:
1) Introduce a common backend design component: rate limiting.
2) Show how a high-level design can be simulated in pure Python.
3) Connect system design concepts (throughput, burst, refill) to code.

Important note:
- This is an educational *sketch*, not production-ready infrastructure.
- Real deployments may require distributed state, strong consistency,
  observability, persistence, and eviction strategies.
"""

from dataclasses import dataclass
import time


@dataclass
class TokenBucket:
    """
    Token bucket for one client/user/key.

    Concepts:
    - capacity: maximum burst allowed.
    - refill_rate_per_sec: tokens added per second over time.
    - tokens: current available tokens.
    - last_refill_ts: when refill was last computed.
    """

    capacity: float
    refill_rate_per_sec: float
    tokens: float
    last_refill_ts: float

    def refill(self, now: float) -> None:
        """
        Refill tokens based on elapsed time.

        Formula:
        new_tokens = elapsed_seconds * refill_rate_per_sec
        tokens = min(capacity, tokens + new_tokens)
        """
        elapsed = max(0.0, now - self.last_refill_ts)
        added = elapsed * self.refill_rate_per_sec
        self.tokens = min(self.capacity, self.tokens + added)
        self.last_refill_ts = now

    def allow(self, cost: float, now: float) -> bool:
        """
        Attempt to consume `cost` tokens.

        Returns True if request is allowed, otherwise False.
        """
        self.refill(now)
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


class InMemoryRateLimiter:
    """
    Educational in-memory limiter keyed by user/client id.

    System design discussion points:
    - In memory is simple but single-node.
    - In distributed systems, shared stores (e.g. Redis) are common.
    - You may also need TTL cleanup to avoid unbounded key growth.
    """

    def __init__(self, capacity: float, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.buckets: dict[str, TokenBucket] = {}

    def _get_bucket(self, key: str, now: float) -> TokenBucket:
        # Lazily create bucket at first request for that key.
        if key not in self.buckets:
            self.buckets[key] = TokenBucket(
                capacity=self.capacity,
                refill_rate_per_sec=self.refill_rate_per_sec,
                tokens=self.capacity,
                last_refill_ts=now,
            )
        return self.buckets[key]

    def allow_request(self, key: str, cost: float = 1.0) -> bool:
        """
        Public API: check if request from `key` can pass.

        cost allows weighted requests:
        - simple endpoint might cost 1 token
        - expensive endpoint might cost >1 tokens
        """
        now = time.monotonic()
        bucket = self._get_bucket(key, now)
        return bucket.allow(cost=cost, now=now)


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Example scenario
    # ------------------------------------------------------------
    # Configure limiter: burst up to 5 requests, refill 1 token/sec.
    limiter = InMemoryRateLimiter(capacity=5, refill_rate_per_sec=1)
    user = "student-123"

    print("Initial burst test (7 quick requests):")
    for i in range(7):
        allowed = limiter.allow_request(user)
        print(f"request {i + 1}: {'ALLOWED' if allowed else 'BLOCKED'}")

    print("\nSleeping 2.5 seconds to refill some tokens...")
    time.sleep(2.5)

    print("After refill:")
    for i in range(3):
        allowed = limiter.allow_request(user)
        print(f"request {i + 1}: {'ALLOWED' if allowed else 'BLOCKED'}")

    print("\nDesign extension ideas:")
    print("- Store buckets in Redis for multi-instance apps.")
    print("- Add per-endpoint limits and per-user tiers.")
    print("- Emit metrics for blocked requests and remaining tokens.")