from django.urls import path, include
from .views import *

# Main Urls
app_name = 'main'

urlpatterns = [
    path('', index.as_view(), name='index')
]
