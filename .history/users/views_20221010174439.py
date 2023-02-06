from multiprocessing import context
from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context
    
    return  render(request,"users/profiles.html")

