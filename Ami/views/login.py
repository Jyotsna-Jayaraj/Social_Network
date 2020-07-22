from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

class Login(View):
	def get(self, request):
		return render(request, "Ami/login.html")

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.error(request, 'Invalid Credentials!')
			return redirect('login')
