from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path("careers/", PostListCreateView.as_view(), name="post-list-create"),
    path("careers/<int:pk>/", PostDetailView.as_view(), name="post-update-delete"),
]