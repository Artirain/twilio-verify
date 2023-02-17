from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.TextField(max_length=20, blank=False) #добавляем атрибут phone
    is_verified = models.BooleanField(default=False) #атрибут, верефицирован ли юзер