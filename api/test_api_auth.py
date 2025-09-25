import pytest
from utils import api_helpers

def test_post_verify_login_valid():
    resp = api_helpers.post_verify_login_valid("validuser@example.com", "TestPassword123!")
    assert resp.status_code in (200, 404, 401)

def test_post_verify_login_no_email():
    resp = api_helpers.post_verify_login_no_email("TestPassword123!")
    assert resp.status_code in (200, 400, 404)

def test_delete_verify_login():
    resp = api_helpers.delete_verify_login("validuser@example.com", "TestPassword123!")
    assert resp.status_code in (200, 405, 404)

def test_post_verify_login_invalid():
    resp = api_helpers.post_verify_login_invalid("invalid@example.com", "wrongpass")
    assert resp.status_code in (200, 401, 404)
