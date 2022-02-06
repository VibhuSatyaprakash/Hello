from django.db import models
from django.utils import timezone
class Post(models.Model):
    tasks=models.TextField()
    datetime=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.tasks} | {self.datetime}"
# Create your models here.
