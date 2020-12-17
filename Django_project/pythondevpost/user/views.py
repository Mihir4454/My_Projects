from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdationForm
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    # form = UserCreationForm()
    # return render(request, "user/register.html",{"user_form":form})

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            user = User.objects.get(username=username)
            sendConfirm(user)
            messages.success(request,f'Hi, {username}: Your account created successfully, Please varify your Email adress')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html",{"user_form":form})


def profile(request):
    
    if request.method == 'POST':
        p_form = UserUpdationForm(request.POST, instance =request.user)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = UserUpdationForm(instance =request.user)

    
    return render(request, "user/profile.html",{"p_form":p_form})


