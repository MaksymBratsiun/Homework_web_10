from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=60, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField(max_length=200)
    born_location = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.CharField(max_length=1500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.quote}'
