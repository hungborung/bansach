from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import MyUserCreationForm, MyUserChangeForm, ProfileForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm


def signup(request):    
    form = MyUserCreationForm()
   
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=request.POST['password1'] )
            login(request, user)
            return redirect('home')
            
    return render(request, 'signup.html', { 'form':  form})


@login_required
def account(request):
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')


    context = {
        'form': form,
        
        'user': user,
    }

    return render(request, 'profile/general.html', context)
    

@login_required
def userorder(request):
    return render(request, 'profile/userorder.html')

@login_required
def notification(request):
    return render(request, 'profile/notification.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, 'profile/password.html', context)