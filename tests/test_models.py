"""Model round-trip tests for prisma_browser (generated; per-product)."""

from prisma_browser.models.bulk_created_item import BulkCreatedItem


def test_bulk_created_item_round_trip() -> None:
    data = {"id": "abc-123", "name": "test-resource"}
    obj = BulkCreatedItem.from_dict(data)
    assert obj is not None
    assert obj.to_dict()  # round-trips to a dict
