"""Errors component smoke tests (generated)."""

from prisma_browser.exceptions import ApiException
from prisma_browser.extras import errors


def test_errors_helpers() -> None:
    assert callable(errors.error_message)
    assert issubclass(errors.RateLimitException, ApiException)
