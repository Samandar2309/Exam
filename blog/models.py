from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="teams")

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=212)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HappyClients(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to="happy_clients")

    def __str__(self):
        return self.name
