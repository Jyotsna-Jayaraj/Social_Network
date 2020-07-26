from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

from Ami.models import Group

class CreateGroup(View):
	def get(self, request):
		if request.user.is_authenticated:
			return render(request, "Ami/groups_create.html")   
		else:
			messages.error(request, "Please login first!")
			return redirect('login')
	
	def post(self, request):
		name = request.POST.get('groupname')
		description = request.POST.get('groupdesc')

		try:
			new_group = Group.objects.create(name=name, description=description, creator=request.user)
			new_group.save()
			messages.success(request, "Group Created!")
			return redirect('view-group', new_group.slug)
		except IntegrityError:
			messages.error(request, "Group name already exists!")
			return redirect('create-group')
		except Exception as e:
			print(e)
			messages.error(request, "Something went wrong!")
			return redirect('create-group')
		


