from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField(max_length=200)
    born_location = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Quote(models.Model):
    quote = models.CharField(max_length=1500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)

