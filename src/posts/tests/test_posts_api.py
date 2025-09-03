import re
import pytest
from django.urls import reverse
from posts.models import Posts

DATETIME_RE = r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$"

@pytest.mark.django_db
def test_list_empty(api_client):
    url = reverse("post-list-create")
    resp = api_client.get(url)
    assert resp.status_code == 200
    assert resp.data == []  

@pytest.mark.django_db
def test_create_post_success(api_client):
    url = reverse("post-list-create")
    payload = {
        "username": "duanne",
        "title": "Hello",
        "content": "World"
    }
    resp = api_client.post(url, payload, format="json")
    assert resp.status_code == 201
    for key in ["id", "username", "created_at", "title", "content"]:
        assert key in resp.data
    assert resp.data["username"] == "duanne"
    assert re.match(DATETIME_RE, resp.data["created_at"])

@pytest.mark.django_db
def test_create_username_unique_violation(api_client):
    url = reverse("post-list-create")
    payload = {"username": "same", "title": "a", "content": "b"}
    resp1 = api_client.post(url, payload, format="json")
    assert resp1.status_code == 201
    resp2 = api_client.post(url, payload, format="json")
    assert resp2.status_code == 400
    assert "username" in resp2.data

@pytest.mark.django_db
def test_retrieve_detail_returns_full_fields(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    resp = api_client.get(url)
    assert resp.status_code == 200
    for key in ["id", "username", "created_at", "title", "content"]:
        assert key in resp.data
    assert re.match(DATETIME_RE, resp.data["created_at"])

@pytest.mark.django_db
def test_patch_updates_only_title_content(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    payload = {"title": "Novo título", "content": "Novo conteúdo"}
    resp = api_client.patch(url, payload, format="json")
    assert resp.status_code == 200
    post.refresh_from_db()
    assert post.title == "Novo título"
    assert post.content == "Novo conteúdo"

@pytest.mark.django_db
def test_patch_cannot_update_username(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    payload = {"username": "tentativa_de_mudar"}
    resp = api_client.patch(url, payload, format="json")
    assert resp.status_code == 400
    assert "username" in resp.data
    post.refresh_from_db()
    assert post.username == "user1"

@pytest.mark.django_db
def test_put_is_not_allowed(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    resp = api_client.put(url, {"title": "x", "content": "y"}, format="json")
    assert resp.status_code == 405 

@pytest.mark.django_db
def test_post_on_detail_is_not_allowed(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    resp = api_client.post(url, {"foo": "bar"}, format="json")
    assert resp.status_code == 405

@pytest.mark.django_db
def test_method_allow_header(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    resp = api_client.options(url)
    allow = resp.headers.get("Allow") or resp["Allow"]
    for m in ["GET", "PATCH", "DELETE"]:
        assert m in allow
    assert "PUT" not in allow
    assert "POST" not in allow

@pytest.mark.django_db
def test_delete_post(api_client, post):
    url = reverse("post-update-delete", kwargs={"pk": post.id})
    resp = api_client.delete(url)
    assert resp.status_code == 204
    assert not Posts.objects.filter(id=post.id).exists()
