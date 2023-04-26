from typing import Iterable
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password




class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('El Email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    profile_image = models.ImageField(upload_to='perfil/',null=True,blank=True, default='perfil/default.png' )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self,*args, **options ):
        self.password = make_password(self.password)
        # print("as ", super().save(*args, **kwargs))
        super().save(*args, **options)



    # def save(self, *args, **kwargs):
    #         self.password = make_password(self.password)
    #         super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super(User, self).save(*args, **kwargs)
    
# encriptación de la contraseña al momento 
# de guardar un usuario ya sea el crearse o actualizarse

    # def save(self,**kwargs):
    #     self.password = make_password(self.password)
    #     # print("as ", super().save(*args, **kwargs))
    #     return super().save(**kwargs)

    

        # def save(self,*args, **kwargs):
        #     self.password = make_password(self.password)
        #     return super().save(*args, **kwargs)

    

    # is_administrator  = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(default=timezone.now)
    # receive_newsletter = models.BooleanField(default=False)
    # birth_date = models.DateTimeField(blank=True, null=True)
    # address = models.CharField(max_length=300,  blank=True, null=True)
    # city = models.CharField(max_length=30, blank=True, null=True)
    # about_me = models.TextField(max_length=500, blank=True, null=True)




