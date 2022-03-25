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

def login(request):
    return render(request, 'registration/login.html')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return logout