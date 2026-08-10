from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly


class BlogListCreateAPIView(generics.ListCreateAPIView):

    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "title",
        "content",
    ]

    ordering_fields = [
        "created_at",
        "number_of_views",
    ]

    ordering = [
        "-created_at",
    ]
    filterset_fields = [

"isPublished",

"author",

]

    def perform_create(self, serializer):

        serializer.save(
            author=self.request.user
        )


class BlogRetrieveUpdateDestroyAPIView(

    generics.RetrieveUpdateDestroyAPIView

):

    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    permission_classes = [
        IsAuthorOrReadOnly
    ]