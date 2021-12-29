from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    UserType = [
        ('researcher', 'Researcher'),
        ('subject', 'Subject'),

    ]
    type = models.CharField(choices=UserType, max_length=200, null=True, blank=True)


class News(models.Model):
    source = models.TextField( null=True, blank=True)
    author = models.TextField( null=True, blank=True)
    title = models.TextField( null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True, max_length=1000)
    urlToImage = models.URLField(null=True, blank=True, max_length=1000)
    publishedAt = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)


class ProjectNews(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    highlight = JSONField()
