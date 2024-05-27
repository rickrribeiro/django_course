from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# uma boa pratica é criar um manager para o model de usuário

class UserManager(BaseUserManager):
    def normalize_email(self, email):
        normalized_email = super().normalize_email(email)
        return normalized_email.lower()
        
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # to asign a user manager

    USERNAME_FIELD = 'email'
    

