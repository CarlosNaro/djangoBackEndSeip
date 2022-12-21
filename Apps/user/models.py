from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField( max_length=250)
    email = models.CharField(unique=True, max_length=250)
    first_name = models.CharField(blank=True, null=True, max_length=250)
    last_name = models.CharField(blank=True, null=True, max_length=250)
    is_active = models.BooleanField(default=True)  
    is_administrator = models.BooleanField(default=False)
    # password
    # imagen = models.ImageField(upload_to='perfil/',blank=True, null=True, max_length=250,)
    # date_joined = models.DateField( auto_now_add=True)
    # last_login

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name},{self.last_name}'
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_administrator



class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,first_name, last_name,password = None ):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        usuario = self.model(
            username = username, 
            email=self.normalize_email(email),
            nombre = first_name,
            apellidos = last_name
            )

        usuario.set_password(password)
        usuario.save()
        return 

    def create_superuser(self,email,username,first_name, last_name,password):
        usuario = self.create_user(
            email,
            username = username, 
            nombre = first_name,
            apellidos = last_name
        )
        usuario.is_administrator = True
        usuario.save()
        return usuario


