from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,blank = True)
    name = models.CharField(max_Length = 200, blank=True, null=True)
    email = models.CharField(max_Length = 200, blank=True, null=True)
    short_int = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)
     = models.CharField(max_Length = 200, blank=True, null=True)