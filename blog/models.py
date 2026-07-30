from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="blogs"
)
    title = models.CharField(
        max_length=200
    )

    content = models.TextField()
    image = models.ImageField(
             upload_to="blog_images/",
             blank=True,
             null=True,)


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(auto_now=True)
    isPublished = models.BooleanField(default=False)
    number_of_views = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
    
            return self.title



class Comment(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    content = models.TextField()
    

     


    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.author.username} - {self.blog.title}"    
    
    
