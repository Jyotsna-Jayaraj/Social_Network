from django.views import View
from django.shortcuts import render, redirect

from Ami.models import Group, GroupMember, Post

class CreatePost(View):
	def get(self, request):
		groups = [obj.group for obj in GroupMember.objects.filter(user=request.user)] 
		context = {'groups': groups}
		return render(request, "Ami/posts_create.html", context)
	
	def post(self, request):
		message = request.POST.get('message')
		group = Group.objects.get(name=request.POST.get('groupname'))
		user = request.user

		try:
			new_post = Post(message=message, user=user, group=group)
			new_post.save()
			return redirect('view-group', group.slug)
		except Exception as e:
			print(e)
			return redirect('create-post')

