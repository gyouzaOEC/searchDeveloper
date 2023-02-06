from multiprocessing import context
from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all("profiles":profiles)
    context = {"profiles":profiles}
    
    return  render(request,"users/profiles.html")"profiles:profiles"

