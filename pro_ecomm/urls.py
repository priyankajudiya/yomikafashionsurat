from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# Main Urls

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('user/', include('app_user.urls')),
    path('ajax/', include('app_ajax.urls')),
    path('myprofile/', include('app_profile.urls')),
    path('products/', include('app_products.urls')),
    path('shopping/myCart/', include('app_cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
