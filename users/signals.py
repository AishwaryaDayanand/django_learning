from django.contrib.auth.models import User
# signals
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from .models import Profile

# @receiver(post_delete,sender=Profile )
def deleteUser(sender, instance,**kwargs):
    user = instance.user
    user.delete()
# @receiver(post_save,sender=User)
def createProfile(sender, instance , created,**kwargs):
    print("profile created /updated")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email
        )



post_save.connect(createProfile , sender=User)
post_delete.connect(deleteUser , sender=Profile)
