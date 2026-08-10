from rest_framework import serializers
from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = [
            'id',
            'author',
            'title',
            'content',
            'image',
            'created_at',
            'updated_at',
            'isPublished',
            'number_of_views',
        ]


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'