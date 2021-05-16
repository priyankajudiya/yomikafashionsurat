from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from . import models

class registrationUserForm(ModelForm):
    class Meta():
        model = User
        fields = ('email',)

class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'