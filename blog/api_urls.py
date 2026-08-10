from django.urls import path
from .api_views import (
    BlogListCreateAPIView,
    BlogRetrieveUpdateDestroyAPIView,
)

urlpatterns = [

    path(
        'blogs/',
        BlogListCreateAPIView.as_view(),
        name='api_blog_list_create',
    ),

    path(
        'blogs/<int:pk>/',
        BlogRetrieveUpdateDestroyAPIView.as_view(),
        name='api_blog_detail',
    ),

]