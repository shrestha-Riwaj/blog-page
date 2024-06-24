from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body =models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish', )
        db_table = "posts"

    def __str__(self):
        return self.title