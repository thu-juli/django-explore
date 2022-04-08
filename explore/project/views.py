from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project/project-form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }

    return render(request, 'project/project-form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'project': project,
    }

    return render(request, 'project/delete-project.html', context)
