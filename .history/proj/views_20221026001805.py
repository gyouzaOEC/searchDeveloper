import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm,ReviewForm
from .utils import searchProjects,paginationProjects

# Create your views here.



def projects(request):
    
    projects,search_query = searchProjects(request)    
    custom_range,projects = paginationProjects(request,projects, 3)
    
    contenxt = {"projects":projects,"search_query":search_query,
                "custom_range":custom_range}
    
    return render(request,"proj/projects.html",contenxt)


def project(request,pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    
    if request.method =="POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        
        project.getVoteCount
        
        messages.success(request, "Your review was successfully submitted.")
        return redirect("projects", pk = project.id)
    
    contenxt = {"project":project,"form":form}
    return render(request,"proj/single-project.html",contenxt)


@login_required(login_url="login")
def createProject(request,):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect("account")
    
    contenxt = {"form":form}
    return render(request,"proj/project_form.html",contenxt)



@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("account")
    
    contenxt = {"form":form}
    return render(request,"proj/project_form.html",contenxt)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
        
    context= {"object":project}
    return render(request,"delete-template.html",context)
