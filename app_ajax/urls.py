from django.urls import path, include
from .views import *

# Main Urls
app_name = 'ajax'

urlpatterns = [
    path('validate_username', validate_username.as_view(), name='validate_username'),
]
