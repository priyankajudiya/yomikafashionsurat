from django.contrib.auth.models import User
from app_user.models import Profile
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic import View
from . import forms
from django.contrib import messages

# Create your views here.
################################################## Registration View
class userRegistration(View):
    def get(self, request):
        form = forms.registrationUserForm
        context = {
            'form':form,
        }
        return render(request, 'app_user/userRegistration.html', context)

    def post(self, request):
        form = forms.registrationUserForm(request.POST)
         
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.POST.get('email')
            instance.first_name = request.POST.get('first_name')
            instance.last_name = request.POST.get('last_name')
            instance.set_password(request.POST.get('password'))

            try:
                instance.save()
                gen = request.POST.get('gendar')
                user = User.objects.get(username = instance.email)
                pro = Profile.objects.create(user=user, gendar=gen)
                pro.save()
                
                messages.success(request, 'Registration Success')
                
                return redirect('user:userLogin')
            except: 
                return HttpResponse('email already registrade')

################################################## Login View
from django.contrib.auth import login, logout, authenticate
class userLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('myprofile:profileView')
        return render(request, 'app_user/userLogin.html')

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            nxt = request.GET.get('next')
            if nxt:
                return redirect(self.request.GET.get('next'))
            return redirect('main:index')
        else:
            return HttpResponse('Login faild')

# ================================================= LogOut     
def userLogout(request):
    nxt = request.GET.get('next')
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully')
        if nxt:
            return redirect(request.GET.get('next'))
        return redirect('main:index')
    else:
        messages.error(request, 'You are not Logged In')
        return redirect('main:index')
