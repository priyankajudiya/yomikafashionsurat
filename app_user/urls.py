from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

# Main Urls
app_name = 'user'

urlpatterns = [
    path('new/registration', userRegistration.as_view(), name='userRegistration'),
    path('login/', userLogin.as_view(), name='userLogin'),
    path('logout/', userLogout, name='userLogout'),
]
