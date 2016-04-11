from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
