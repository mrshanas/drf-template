from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    email = models.EmailField(unique=True,editable=False)
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True,max_length=200)
    profile_pic = models.URLField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email

    def get_jwt_tokens(self):

        tokens = RefreshToken.for_user(self)

        return {
            'access': str(tokens.access_token),
            'refresh': str(tokens)
        }
