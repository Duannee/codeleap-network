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
class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    http_method_names = ["get", "patch", "delete"]
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostSerializer
        return PostUpdateSerializer
    

