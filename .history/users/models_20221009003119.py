from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,blank = True)
    name = models.CharField(max_Length = 200, blank=True, null=True)
    email = models.CharField(max_Length = 200, blank=True, null=True)
    short_intro = models.CharField(max_Length = 200, blank=True, null=True)
    bio = models.CharField(max_Length = 200, blank=True, null=True)
    profile_image = models.CharField(max_Length = 200, blank=True, null=True)
    social_ = models.CharField(max_Length = 200, blank=True, null=True)
    social_ = models.CharField(max_Length = 200, blank=True, null=True)
    social_ = models.CharField(max_Length = 200, blank=True, null=True)
    social_ = models.CharField(max_Length = 200, blank=True, null=True)
    social_ = models.CharField(max_Length = 200, blank=True, null=True)