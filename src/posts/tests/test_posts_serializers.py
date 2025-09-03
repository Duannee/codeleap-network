import re
import pytest
from posts.serializers import PostSerializer, PostUpdateSerializer
from posts.models import Posts
from model_bakery import baker

DATETIME_RE = r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$"

@pytest.mark.django_db
def test_post_serializer_output_format_created_at():
    post = baker.make(Posts, username="u1", title="t", content="c")
    data = PostSerializer(post).data
    assert set(["id", "username", "created_at", "title", "content"]).issubset(data.keys())
    assert re.match(DATETIME_RE, data["created_at"])

def test_post_update_serializer_blocks_username():
    ser = PostUpdateSerializer(data={"username": "x", "title": "t", "content": "c"}, partial=True)
    assert not ser.is_valid()
    assert "username" in ser.errors

def test_post_update_serializer_accepts_title_content_only():
    ser = PostUpdateSerializer(data={"title": "novo", "content": "novo"}, partial=True)
    assert ser.is_valid()
