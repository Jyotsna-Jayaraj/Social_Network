from django.views import View
from django.shortcuts import render

from Ami.models import GroupMember

class CreatePost(View):
	def get(self, request):
		groups = [obj.group for obj in GroupMember.objects.filter(user=request.user)] 
		context = {'groups': groups}
		return render(request, "Ami/posts_create.html", context)