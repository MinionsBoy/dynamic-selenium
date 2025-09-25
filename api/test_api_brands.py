import pytest
from utils import api_helpers

def test_get_all_brands():
    resp = api_helpers.get_all_brands()
    assert resp.status_code in (200, 404)

def test_put_all_brands():
    resp = api_helpers.put_all_brands()
    assert resp.status_code in (200, 405)
