from django.urls import path
from .views import (
    home, 
    about, 
    PostListView, 
    PostDetailView, 
    PostCreateView
    )

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", about, name="blog-about")

]