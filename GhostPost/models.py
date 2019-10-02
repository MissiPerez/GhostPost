from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    published_date = models.DateTimeField(auto_now_add=True)
    boast = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.title} - {self.author}"
