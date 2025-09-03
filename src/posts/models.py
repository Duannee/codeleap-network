from django.db import models

class Posts(models.Model):
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self) -> str:
        return f"Post by {self.username}"
