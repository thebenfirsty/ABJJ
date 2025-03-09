from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return HttpResponse("Hello from the Core App!")


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form', form})


def profile_detail(request, username):
    user_obj = get_object_or_404(User, username=username)
    return render(request, 'profile_detail.html', {'user_obj': user_obj})

