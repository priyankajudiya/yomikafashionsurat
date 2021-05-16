from typing import Tuple
from django.db import models
from django.contrib.auth.models import User

from datetime import date

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gendar = models.CharField(max_length=7, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)

    list_display = list_display = ('pk', 'user', 'gendar', 'dob', 'age')

    @property
    def age(self):
        if self.dob != None:
            age = date.today().year - self.dob.year
            return age
