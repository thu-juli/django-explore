from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {
        'projectlist': projects,
    }
    return render(request, 'project/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'project/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'project/project-form.html', context)
