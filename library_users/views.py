from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from . import forms
from .forms  import UserForm, UserProfileinfoForm
from django.urls import reverse,resolve
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect

import library_users

# Create your views here.

def the_index(request):
    mydect2 = {'name2':'This is yje index page of Library users app !!  '}
    return render(request, "library_users/index.html",context=mydect2)


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileinfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileinfoForm()

    return render(request, "library_users/registration.html",context=
                                        {'registered':registered,'user_form': user_form, 'profile_form': profile_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('books:landing'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)     

        if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('books:view_books'))
                else:
                    return HttpResponse("Account Not Active")
        else:
                print("someone tried to ogin and failled")         
                return HttpResponse('invalid username supplied')
    else:
        return render(request,"library_users/login.html",{})    