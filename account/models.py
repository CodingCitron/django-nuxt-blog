from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt

class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    nickname = models.CharField(max_length=50)

class ActiveUser(models.Model):
    pass