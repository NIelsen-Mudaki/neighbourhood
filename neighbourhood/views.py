from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', locals())

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Admin = current_user
            project.admin_profile = profile
            project.save()
        return redirect('index')

    else:
        form = NewBusinessForm()
    return render(request, 'new-business.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = request.user.profile
    neighborhood = request.user.profile.neighborhood

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.author_profile = profile
            post.neighborhood = neighborhood
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_for_businesses(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"businesses": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form2 = NewNeighborhoodForm(request.POST)
        
        if form2.is_valid():
            neighborhood = form2.save(commit=False)
            neighborhood.Admin = current_user
            neighborhood.admin_profile = profile
            neighborhood.save()
            return redirect('profile')
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
            
    else:
        form = ProfileUpdateForm()
        form2 = NewNeighborhoodForm()

    return render(request, 'profile.html', {"form":form, "form2":form2})

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return logout