import pytest
from utils import api_helpers

def test_get_all_products():
    resp = api_helpers.get_all_products()
    assert resp.status_code in (200, 404)

def test_post_all_products():
    resp = api_helpers.post_all_products()
    assert resp.status_code in (200, 405)

def test_get_product_detail():
    resp = api_helpers.get_product_detail(1)
    assert resp.status_code in (200, 404)

def test_search_products():
    resp = api_helpers.search_products("Tshirt")
    assert resp.status_code in (200, 404)

def test_post_search_products():
    resp = api_helpers.post_search_products("Tshirt")
    assert resp.status_code in (200, 405)

def test_post_search_products_no_param():
    resp = api_helpers.post_search_products_no_param()
    assert resp.status_code in (200, 405)
