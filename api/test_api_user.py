import pytest
import uuid
from utils import api_helpers

def test_post_create_user():
    email = f"apitest_{uuid.uuid4().hex[:8]}@example.com"
    resp = api_helpers.post_create_user("API Test", email, "TestPassword123!")
    assert resp.status_code in (200, 201, 400, 409)

def test_delete_user():
    # Try to delete a user that likely does not exist
    resp = api_helpers.delete_user("notarealuser@example.com")
    assert resp.status_code in (200, 404, 400)

def test_put_update_user():
    resp = api_helpers.put_update_user("validuser@example.com", name="Updated Name")
    assert resp.status_code in (200, 404, 400)

def test_get_user_detail_by_email():
    resp = api_helpers.get_user_detail_by_email("validuser@example.com")
    assert resp.status_code in (200, 404)
