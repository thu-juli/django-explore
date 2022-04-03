from django.shortcuts import render
from .models import Project


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    projects = Project.objects.all()
    content = {
        'projectlist': projects,
    }
    return render(request, 'project/projects.html', content)


def project(request, pk):

    projectObj = Project.objects.get(id=pk)

    return render(request, 'project/single-project.html', {'project': projectObj})
