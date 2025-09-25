import pytest
from utils import api_helpers

def test_get_all_categories():
    resp = api_helpers.get_all_categories()
    assert resp.status_code in (200, 404)
