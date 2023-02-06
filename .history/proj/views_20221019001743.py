from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
# Create your views here.



def projects(request):
    projects = Project.objects.all()
    contenxt = {"projects":projects}
    return render(request,"proj/projects.html",contenxt)


def project(request,pk):
    project = Project.objects.get(id=pk)
    contenxt = {"project":project}
    return render(request,"proj/single-project.html",contenxt)


@login_required(login_url="login")
def createProject(request,):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project
            form.save()
            return redirect("projects")
    
    contenxt = {"form":form}
    return render(request,"proj/project_form.html",contenxt)



@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    
    contenxt = {"form":form}
    return render(request,"proj/project_form.html",contenxt)

@login_required(login_url="login")
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
        
    context= {"object":project}
    return render(request,"proj/delete-project.html",context)
