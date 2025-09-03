import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from posts.models import Posts

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def post(db):
    return baker.make(Posts, username="user1", title="T1", content="C1")
