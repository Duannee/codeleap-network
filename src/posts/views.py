from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    
)
from .models import Posts
from .serializers import PostSerializer, PostUpdateSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Posts"])
class PostListCreateView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

@extend_schema(tags=["Posts"])
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostUpdateSerializer

    http_method_names = ["get", "patch", "delete"]

