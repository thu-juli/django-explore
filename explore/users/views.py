from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    # listProject = Project.objects.all()

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
        # 'listProject': listProject,
    }
    return render(request, 'users/user-profile.html', context)
