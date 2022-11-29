from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name,username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name,username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
 
    ROLE_CHOICE = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer'),
    )
 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100,  unique= True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
 
    # Required Fields

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
 
    objects = UserManager()
 
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='user/profile_photo',blank=False)
    cover_photo=models.ImageField(upload_to='user/cover_photo',blank=False)
    address_line1=models.CharField(max_length=255)
    address_line2=models.CharField(max_length=255)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    pinCode=models.BigIntegerField(blank=True,null=True,)
    latitude=models.FloatField(blank=True,null=True)
    longtitude=models.FloatField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modeified_date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.user.email


