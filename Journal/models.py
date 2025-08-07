from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True, null=True)
    entry = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.heading} - {self.user.username} ({self.date})"

    class Meta:
        ordering = ['-date', '-created_at']


