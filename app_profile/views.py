from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from app_user.models import Profile
from django.contrib.auth.models import User

# Create your views here.


class profileView(View):
    def get(self, request):
        return render(request, 'app_profile/profileView.html')

    def post(self, request):
        user = User.objects.get(pk = request.user.pk)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        obj = Profile.objects.get(user = request.user)
        obj.phone_number = request.POST.get('phone_number')
        obj.gendar = request.POST.get('gendar')
        obj.address = request.POST.get('address')
        obj.dob = request.POST.get('dob')
        obj.state = request.POST.get('state')
        obj.city = request.POST.get('city')
        obj.pincode = request.POST.get('pincode')
        obj.save()
        
        return redirect('myprofile:profileView')
