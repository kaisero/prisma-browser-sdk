"""Facade component smoke tests (generated)."""

from prisma_browser.extras.facade import Client


def test_facade_client_api() -> None:
    assert hasattr(Client, "from_env")
    assert hasattr(Client, "from_credentials")
    assert hasattr(Client, "paginate")

