"""Retry with jitter (vendored by phantasos). Subclasses urllib3's Retry; jitter is
applied in get_backoff_time(); Retry-After handling stays urllib3's."""

from __future__ import annotations

import random

from urllib3.util.retry import Retry

__all__ = ["JitteredRetry", "default_retry"]


class JitteredRetry(Retry):
    """urllib3 Retry with cloudflare-style multiplicative jitter on the backoff.

    Reuses urllib3's own ``backoff_factor`` (base) and ``backoff_max`` (cap) — set via
    ``default_retry()`` so they survive ``Retry.new()`` cloning — and applies multiplicative
    jitter here. Only ``jitter_frac`` is phantasos-specific.
    """

    jitter_frac = 0.25

    def get_backoff_time(self) -> float:
        # Count the most recent consecutive run of non-redirect errors (urllib3's intent).
        consecutive = 0
        for h in reversed(self.history):
            if h.redirect_location is not None:
                break
            consecutive += 1
        if consecutive <= 1:
            return 0.0
        exp = min(self.backoff_factor * (2 ** (consecutive - 1)), self.backoff_max)
        return exp * (1 - self.jitter_frac * random.random())


def default_retry() -> JitteredRetry:
    """The SDK's default retry policy (on by default, wired by the facade/auth)."""
    return JitteredRetry(
        total=3,
        status_forcelist=[408, 429, 500, 502, 503, 504],
        backoff_factor=0.5,
        backoff_max=8.0,
        allowed_methods=None,
        respect_retry_after_header=True,
        raise_on_status=False,
    )
