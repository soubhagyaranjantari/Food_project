from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import userProfile,User


@receiver(post_save, sender=User)
def post_save_user_profile(sender,instance,created=None,**kwargs):
    print(created)
    if created:
        userProfile.objects.create(user=instance)
        print("User and user profile is created")

    #if occures any error while modifying userprofile
    else:
        pass
        # try:
        #     profile = userProfile.objects.create(user=instance)
        #     profile.save()
        # except:
        #     userProfile.objects.create(user=instance)
        # print("User and user profile is not found, So Created One")
