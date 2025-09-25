import pytest
from utils import api_helpers

def test_get_all_products_real():
    resp = api_helpers.get_all_products()
    assert resp.status_code == 200
    assert "products" in resp.text

def test_get_product_detail_real():
    resp = api_helpers.get_product_detail(1)
    assert resp.status_code == 200
    assert "product" in resp.text

def test_search_products_real():
    resp = api_helpers.search_products("Tshirt")
    assert resp.status_code == 200
    assert "products" in resp.text

def test_get_all_brands_real():
    resp = api_helpers.get_all_brands()
    assert resp.status_code == 200
    assert "brands" in resp.text

def test_get_all_categories_real():
    resp = api_helpers.get_all_categories()
    assert resp.status_code == 200
    assert "categories" in resp.text

def test_get_product_detail_not_found_real():
    resp = api_helpers.get_product_detail(999999)
    assert resp.status_code in (200, 404)
