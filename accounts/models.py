from django.db import models
from  django.contrib.auth.models import AbstractUser
from .UserManager import CustomUserManager


class UserProfile(AbstractUser):
    username = None
    PhoneNumber=models.CharField(max_length=11,null=True,blank=True)
    ProfileImage=models.ImageField(upload_to="ProfilImage/image",null=True,blank=True)
    email=models.EmailField(max_length=30,unique=True)
    Address=models.TextField(null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects =  CustomUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    def __str__(self):
        return  self.email