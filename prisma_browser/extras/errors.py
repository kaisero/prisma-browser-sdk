"""Error helpers over the generated typed exceptions (vendored by phantasos)."""

from __future__ import annotations

import json
from typing import Any

from ..exceptions import (  # noqa: F401  (re-exported)
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    RateLimitException,
    ServiceException,
    UnauthorizedException,
)

__all__ = [
    "ApiException",
    "BadRequestException",
    "UnauthorizedException",
    "ForbiddenException",
    "NotFoundException",
    "RateLimitException",
    "ServiceException",
    "error_message",
]


def error_message(exc: ApiException) -> str:
    """Extract a human-readable message from an ApiException's JSON error body."""
    body = getattr(exc, "body", None) or getattr(exc, "data", None)
    if isinstance(body, (bytes, bytearray)):
        body = body.decode("utf-8", "replace")
    if isinstance(body, str) and body.strip():
        try:
            body = json.loads(body)
        except ValueError:
            return body.strip()[:500]
    if isinstance(body, dict):
        err = body.get("error")
        if isinstance(err, dict) and isinstance(err.get("message"), str):
            code = err.get("code")
            return f"{code}: {err['message']}" if code else err["message"]
        for key in ("message", "detail", "title"):
            if isinstance(body.get(key), str):
                return body[key]
    return getattr(exc, "reason", None) or "request failed"
