from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(
        max_length=128
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        blank=False, null=False
    )
    body = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.title
