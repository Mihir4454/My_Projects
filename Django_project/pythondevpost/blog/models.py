from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    

