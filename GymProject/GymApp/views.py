from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def classes(request):
    return render(request, 'classes.html')

def trainers(request):
    return render(request, 'trainers.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['new-username']
        email = request.POST['email']
        password = request.POST['new-password']
        confirm_password = request.POST['confirm-password']
        birthday = request.POST['birthday']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create a UserProfile for the user
        UserProfile.objects.create(user=user, birthday=birthday)

        login(request, user)
        return redirect('home')  # Redirect to your home page after registration

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your home page after login
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'home.html')

def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile) 
    
    return render(request, 'edit_profile.html', {'form': form})

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})
