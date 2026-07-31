"""
System Design (Python sketch): Token Bucket Rate Limiter (in-memory).

Educational goals:
1) Introduce rate limiting (burst, steady refill, weighted requests).
2) Connect design concepts to code: throughput, bursts, refill math.
3) Show *sketch-level* extensions: TTL cleanup, pluggable clock, concurrency notes.

Important note:
- This is an educational sketch, NOT production-ready.
- Real systems may need distributed state (e.g., Redis), stronger consistency,
  observability, sharding, persistence, and robust eviction strategies.
"""

from __future__ import annotations

from dataclasses import dataclass
import time
from threading import Lock
from typing import Callable, Optional


# =============================================================================
# 1) Core data structure: TokenBucket
# =============================================================================

@dataclass
class TokenBucket:
    """
    Token bucket for one client/user/key.

    Concepts:
    - capacity: maximum burst allowed
    - refill_rate_per_sec: tokens added per second
    - tokens: current available tokens
    - last_refill_ts: last time we computed refill
    - last_seen_ts: last time this bucket was accessed (useful for TTL eviction)
    """
    capacity: float
    refill_rate_per_sec: float
    tokens: float
    last_refill_ts: float
    last_seen_ts: float

    def refill(self, now: float) -> None:
        """
        Refill tokens based on elapsed time since last_refill_ts.

        Formula:
        added = elapsed_seconds * refill_rate_per_sec
        tokens = min(capacity, tokens + added)
        """
        elapsed = max(0.0, now - self.last_refill_ts)
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate_per_sec)
            self.last_refill_ts = now

    def allow(self, cost: float, now: float) -> bool:
        """
        Attempt to consume `cost` tokens.

        Returns:
        - True if request is allowed (tokens >= cost)
        - False otherwise
        """
        if cost <= 0:
            raise ValueError("cost must be positive")

        self.last_seen_ts = now
        self.refill(now)

        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

    def remaining(self, now: float) -> float:
        """Read-only helper: remaining tokens after refilling to 'now'."""
        self.refill(now)
        return self.tokens


# =============================================================================
# 2) In-memory rate limiter keyed by id
# =============================================================================

class InMemoryRateLimiter:
    """
    Educational in-memory limiter keyed by user/client id.

    Design discussion points:
    - Single-node in-memory state: simple but not horizontally scalable.
    - Concurrency: needs locking if accessed by multiple threads.
    - Key growth: you want eviction (TTL cleanup) to avoid unbounded memory.

    API:
    - allow_request(key, cost=1.0) -> bool
    - remaining_tokens(key) -> float
    - cleanup() -> int (evicted buckets)
    """

    def __init__(
        self,
        capacity: float,
        refill_rate_per_sec: float,
        *,
        ttl_seconds: float = 10 * 60,
        cleanup_every_n_requests: int = 500,
        now_fn: Optional[Callable[[], float]] = None,
    ):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        if refill_rate_per_sec <= 0:
            raise ValueError("refill_rate_per_sec must be positive")
        if ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")
        if cleanup_every_n_requests <= 0:
            raise ValueError("cleanup_every_n_requests must be positive")

        self.capacity = float(capacity)
        self.refill_rate_per_sec = float(refill_rate_per_sec)
        self.ttl_seconds = float(ttl_seconds)
        self.cleanup_every_n_requests = int(cleanup_every_n_requests)

        # Use a pluggable clock for testing/simulation (default: monotonic time).
        self._now: Callable[[], float] = now_fn or time.monotonic

        self._buckets: dict[str, TokenBucket] = {}
        self._lock = Lock()
        self._request_count = 0

    def _get_or_create_bucket(self, key: str, now: float) -> TokenBucket:
        bucket = self._buckets.get(key)
        if bucket is None:
            bucket = TokenBucket(
                capacity=self.capacity,
                refill_rate_per_sec=self.refill_rate_per_sec,
                tokens=self.capacity,        # start full to allow initial burst
                last_refill_ts=now,
                last_seen_ts=now,
            )
            self._buckets[key] = bucket
        return bucket

    def allow_request(self, key: str, cost: float = 1.0) -> bool:
        """
        Check if request from `key` can pass.

        cost supports weighted endpoints:
        - cheap endpoint: cost=1
        - expensive endpoint: cost>1
        """
        now = self._now()
        with self._lock:
            self._request_count += 1
            if self._request_count % self.cleanup_every_n_requests == 0:
                self._evict_expired(now)

            bucket = self._get_or_create_bucket(key, now)
            return bucket.allow(cost=cost, now=now)

    def remaining_tokens(self, key: str) -> float:
        """Inspect remaining tokens for key (after refilling)."""
        now = self._now()
        with self._lock:
            bucket = self._buckets.get(key)
            if bucket is None:
                return self.capacity
            return bucket.remaining(now)

    def cleanup(self) -> int:
        """Force eviction pass (useful in demos/tests). Returns number evicted."""
        now = self._now()
        with self._lock:
            return self._evict_expired(now)

    def _evict_expired(self, now: float) -> int:
        """Remove buckets not seen for ttl_seconds."""
        cutoff = now - self.ttl_seconds
        expired_keys = [k for k, b in self._buckets.items() if b.last_seen_ts < cutoff]
        for k in expired_keys:
            del self._buckets[k]
        return len(expired_keys)

    # Optional: tiny observability hook points (sketch)
    # - you could increment counters, emit logs, or publish metrics here.


# =============================================================================
# 3) Demo: burst + refill + weighted costs + TTL cleanup
# =============================================================================

def _demo() -> None:
    # Configure limiter:
    # - capacity 5 (burst up to 5)
    # - refill 1 token/sec (steady throughput)
    limiter = InMemoryRateLimiter(
        capacity=5,
        refill_rate_per_sec=1,
        ttl_seconds=3.0,                 # short TTL so we can show eviction quickly
        cleanup_every_n_requests=10_000, # don't auto-clean in this tiny demo
    )

    user = "student-123"

    print("=== Initial burst test (7 quick requests, cost=1) ===")
    for i in range(7):
        allowed = limiter.allow_request(user, cost=1)
        rem = limiter.remaining_tokens(user)
        print(f"request {i+1}: {'ALLOWED' if allowed else 'BLOCKED'} | remaining ~ {rem:.2f}")

    print("\nSleeping 2.5 seconds to refill some tokens...")
    time.sleep(2.5)

    print("=== After refill (3 requests, cost=1) ===")
    for i in range(3):
        allowed = limiter.allow_request(user, cost=1)
        rem = limiter.remaining_tokens(user)
        print(f"request {i+1}: {'ALLOWED' if allowed else 'BLOCKED'} | remaining ~ {rem:.2f}")

    print("\n=== Weighted requests (cost=2) ===")
    for i in range(3):
        allowed = limiter.allow_request(user, cost=2)
        rem = limiter.remaining_tokens(user)
        print(f"heavy request {i+1}: {'ALLOWED' if allowed else 'BLOCKED'} | remaining ~ {rem:.2f}")

    print("\nSleeping 3.2 seconds to exceed TTL and show eviction...")
    time.sleep(3.2)

    evicted = limiter.cleanup()
    print(f"cleanup() evicted {evicted} bucket(s)")

    # After eviction, the key is treated as new (full burst again)
    print("=== After eviction, bucket is recreated full ===")
    allowed = limiter.allow_request(user, cost=1)
    rem = limiter.remaining_tokens(user)
    print(f"request after eviction: {'ALLOWED' if allowed else 'BLOCKED'} | remaining ~ {rem:.2f}")

    print("\nDesign extension ideas (next steps):")
    print("- Distributed store (Redis) with Lua script for atomic refill+consume.")
    print("- Per-endpoint limits and per-user tiers (different capacity/rates).")
    print("- Observability: counters for allowed/blocked, gauges for remaining tokens.")
    print("- Protection against clock issues (monotonic time already helps).")


if __name__ == "__main__":
    _demo()
