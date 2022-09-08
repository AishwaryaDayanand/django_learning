from multiprocessing import context
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.decorators import login_required


from .forms import ProjectForm
# Create your views here.
def sayHello(request):
    return HttpResponse(" <h1 style='color:red'; > Hello Aish </h1> ") 

def displayProject(request,id):
    project = Project.objects.get(id=id)
    reviews = project.review_set.all()
    techs = project.tags.all()
    context={
        "project":project,
        "reviews":reviews,
        "techs":techs
    }
    return render(request, 'app1/project.html',context) 


def viewProjects(request):
    projects = Project.objects.all()        
    context = {"projects":projects }
    return render(request , 'app1/projects.html',context)

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':  #default method is GET
            project_instance = ProjectForm(request.POST , request.FILES)
            if project_instance.is_valid():
                project_instance.save()
                return redirect("projects")
    context = {'form':form}
    return render(request , 'app1/project_form.html',context)


@login_required(login_url='login')
def updateProject(request , id):
    project = Project.objects.get(id=id)
    update_project_form = ProjectForm(instance=project)  # values are filled
    if request.method == 'POST':  #default method is GET
            project_instance = ProjectForm(request.POST , request.FILES, instance=project)
            if project_instance.is_valid():
                project_instance.save()
                return redirect("projects")
    context = {'form':update_project_form}
    return render(request , 'app1/project_form.html',context)


# confirm delete project
@login_required(login_url='login')
def deleteProject(request , id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {'project' :project }
    return render(request , 'app1/delete_template.html' , context)



# without confirm delete project
@login_required(login_url='login')
def deleteProjectNoConfirm(request , id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')