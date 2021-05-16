from django.contrib.auth.models import User
from django.shortcuts import redirect,  HttpResponse
from django.views.generic import View


# Create your views here.
 
# ======================================= Username Validation
class validate_username(View):
    def get(self, request):
        if request.is_ajax():
            email = request.GET.get('email')
            try:
                is_user = User.objects.get(username = email)
            except:
                is_user = False
            return HttpResponse(bool(is_user))
        else:
            return redirect('main:index')