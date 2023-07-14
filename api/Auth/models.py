# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class AuthUser(AbstractUser):
    username = models.EmailField(_('Email address'), max_length=256, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)

    REQUIRED_FIELDS = ['date_of_birth', 'age']

    objects = UserManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.username}'
