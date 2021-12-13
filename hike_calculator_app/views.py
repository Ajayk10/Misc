from django.shortcuts import render , redirect
#from . models import *
#from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.

def hike(request):
	return render(request, "hike.html" ,{})

def Todo(request):
	return render(request,'Todo.html',{})
