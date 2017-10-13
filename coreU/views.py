# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_jenga')
def home(request):
	user = request.user
	return render(request,'coreU/next.html',{'user': user})

def login_jenga(request):
	form=LoginForm(request.POST)
	if request.method=='POST':
		if request.POST and form.is_valid():
			user=form.login(request)
			if user:
				login(request, user)
				return render(request,'coreU/next.html', {'user':user})
			else:
				return render(request,'coreU/index.html', {'form':form})
	return render(request,'coreU/index.html', {'form':form})
