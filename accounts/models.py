from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, AbstractUser
)

class User(AbstractBaseUser) :
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) # 로그인 할 수 있나? (휴면계정이 아닌가?)
    staff = models.BooleanField(default=False) # superuser가 아닌 staff
    admin = models.BooleanField(default=False) # superuser
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
def __str__(self):
    return self.email

@property
def is_staff(self):
    return self.staff
@property
def is_superuser(self):
    return self.admin


# Create your models here.
