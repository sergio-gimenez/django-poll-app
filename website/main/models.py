from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # Id the user gets deleted, then all the posts made by the user will be deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{}\n{}".format(self.title, self.description)
