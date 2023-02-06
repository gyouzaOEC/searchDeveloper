from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models  import Profile

from django.core.mail import send_mail
from django.core.mail import send_mail


# @receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    print("profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
        )

def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email= profile.email
        user.save()
        
        
        
# @receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()

    
post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)