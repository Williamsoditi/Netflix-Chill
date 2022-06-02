from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from cloudinary.models import CloudinaryField

AGE_CHOICES=(
    ('All', 'All'),
    ('Kids','Kids')
)
MOVIE_CHOICES = (
    ('seasonal','seasonal')
    ('single','single')
)

# Create your models here.
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', null=True, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = CloudinaryField('flyer')
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES)

class Video(models.model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = CloudinaryField('movies')
