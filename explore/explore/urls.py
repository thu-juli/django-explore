from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def project(request, pk):
    return HttpResponse('START PROJECT' + ' ' + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/<int:pk>/', project, name='project'),
]
