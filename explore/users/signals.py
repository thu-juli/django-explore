from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete


def createProfile(sender, instance, created, **kwargs):
    print("Profile signal tiggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
            username=user.username,
            name=user.first_name,
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
