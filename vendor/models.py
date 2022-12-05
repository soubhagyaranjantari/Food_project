from django.db import models
from accounts.models import User, userProfile
# Create your models here.
class vendor_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,unique=False)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # userProfile=models.OneToOneField(userProfile,on_delete=models.CASCADE)
    vendor_name=models.CharField(max_length=50)
    vendor_license=models.ImageField(upload_to='user/license', blank=True)
    is_approved=models.BooleanField(blank=True, null=True)
    created_date=models.DateTimeField(auto_now_add=True,)
    modeified_date=models.DateTimeField(auto_now_add=True)
