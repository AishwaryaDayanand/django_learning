from unicodedata import name
from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from  django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.


def loginPage(request):
    page = 'login'
    context = {
        'page': page
    }
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            # print('username does not exist..')
            messages.error(request, 'username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            # print('username or password is incorrect')
            messages.error(request, 'username or password is incorrect')

    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form  = CustomUserCreationForm()

    if request.method == 'POST':
        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():    
            user  = form.save()
            # user.username = user.username.lower()
            # user.save()
            messages.success(request,"User Registerd Successfully!")
            login(request,user)
            return redirect('profiles')
        
        else:
            messages.success(request,"An Error occured while creating user")

    context = {
        'page': page,
        'form' :form
    }
    return render(request, 'users/login_register.html', context)


def profiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profiles = Profile.objects.filter(name__icontains = search_query)
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    top_skills = user_profile.skill_set.exclude(description__exact="")
    other_skills = user_profile.skill_set.filter(description="")
    context = {
        'profile': user_profile,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'users/user-profile.html', context)



@login_required(login_url='login')
def UserAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request,'users/account.html',context)