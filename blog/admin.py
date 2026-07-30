from django.contrib import admin
from . import models
from .models import Blog, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "author",
        "blog",
        "created_at",
    )

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','isPublished','number_of_views','created_at')
    list_filter = ('isPublished','created_at','title')
admin.site.register(models.Blog, BlogAdmin)