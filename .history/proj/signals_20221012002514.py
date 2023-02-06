from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models  import p



# @receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
        )
# @receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delte()

    
post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)