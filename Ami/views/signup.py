from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from Ami.models import User

class Signup(View):
	def get(self, request):
		return render(request, "Ami/signup.html")

	def post(self, request):
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		
		if password1 != password2:
			messages.error(request, 'Passwords Do Not Match!')
			return redirect('signup')

		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username Already In Use!')
			return redirect('signup')

		try:
			new_user = User(username=username)
			new_user.set_password(password1)
			new_user.save()
		except Exception as e:
			print(e)
			messages.error(request, 'Something Went Wrong!')
			return redirect('login')
		
		messages.success(request, 'Account Created!')
		return redirect('login')