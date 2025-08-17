from django.db import models
from user.models import User
from django.utils import timezone
import uuid

class Status (models.TextChoices):

    draft = "draft",
    published = "published"



class Blog(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.draft)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

