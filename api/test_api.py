import pytest
from utils.api_helpers import get_all_products, get_product_detail, search_products, get_all_brands, get_all_categories

def test_get_all_products():
    response = get_all_products()
    assert response.status_code == 200
    assert "products" in response.text

def test_get_product_detail():
    response = get_product_detail(1)
    assert response.status_code == 200
    assert "product" in response.text

def test_search_products():
    response = search_products("Tshirt")
    assert response.status_code == 200
    assert "products" in response.text

def test_get_all_brands():
    response = get_all_brands()
    assert response.status_code == 200
    assert "brands" in response.text

def test_get_all_categories():
    response = get_all_categories()
    assert response.status_code == 200
    assert "categories" in response.text
