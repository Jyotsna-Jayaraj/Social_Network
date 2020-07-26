from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from Ami.models import Group

class ViewGroup(View):
	def get(self, request, slug):
		group = Group.objects.get(slug=slug)
		context = {'group': group}
		return render(request, "Ami/groups_detail.html", context)