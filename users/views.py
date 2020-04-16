from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'users/home.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User {username} created successfull")
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'users/signup.html',{'form':form})