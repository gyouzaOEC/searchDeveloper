from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST["name"]
        passwor = request.POST["password"]
        
    return  render(request,"users/login_register.html",)
    



def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles":profiles}
    
    return  render(request,"users/profiles.html",context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    
    context = {"profile":profile,"topSkills":topSkills,"otherSkills":otherSkills}

    return  render(request,"users/user-profile.html" ,context)

