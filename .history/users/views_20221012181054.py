from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
# Create your views here.

def loginUser(request):
    if ruquest.user.is_authenticated:
        t
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    
    try:
        usr = User.objects.get(username = username)
        
    except:
        print("Username does not exist")
        
    user = authenticate(request,username=username, password = password)
    
    if user is not None:
        login(request,user)
        return redirect("porfiles")
    
    else:
        print("Username or password is not correct")
        
    return  render(request,"users/login_register.html",)
    
def logoutUser(request):
    logout(request)
    return redirect("login")


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

