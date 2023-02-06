from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.
    
    return  render(request,"users/profiles.html")

