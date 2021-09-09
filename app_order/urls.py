from django.urls import path, include
from django.contrib.auth.decorators import login_required
from.views import *

app_name = 'order'
# Main Urls

urlpatterns = [
    path('checkout', login_required(checkOut.as_view()), name='checkOut'),
]