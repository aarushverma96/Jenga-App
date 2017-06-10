# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from forms import LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
	user=request.user
	if request.user.is_authenticated():
		return render(request,'coreU/next.html',{'user': user})
	else:
		form=LoginForm(request.POST)
		if request.method=='POST':
			if request.POST and form.is_valid():
				user=form.login(request)
				if user:
					login(request,user)
					return render(reuqest,'coreU/next.html',{'user':user})
			else:
				return render(request,'coreU/index.html',{'form':form})
		else:
			return render(request,'coreU/index.html')