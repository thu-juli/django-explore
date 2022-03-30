from django.shortcuts import render


def projects(request):
    return render(request, 'project/projects.html')


def project(request, pk):
    return render(request, 'project/single-project.html')
