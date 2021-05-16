from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import *
# Main Urls
app_name = 'myprofile'
urlpatterns = [
    path('view/', login_required(profileView.as_view()), name='profileView'),
]
