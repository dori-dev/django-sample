from django.db import models
from django.contrib import admin
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

    @admin.display(
        ordering='created',
        description='Created'
    )
    def formatted_datetime(self):
        return self.created.strftime("%B %d, %I:%M %p")

    def __str__(self) -> str:
        return self.title
