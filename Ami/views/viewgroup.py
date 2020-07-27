from django.views import View
from django.shortcuts import render, redirect

from Ami.models import Group, GroupMember

class ViewGroup(View):
	def get(self, request, slug):
		group = Group.objects.get(slug=slug)
		members = [member.user for member in GroupMember.objects.filter(group=group)]
		context = {'group': group, 'members': members}
		return render(request, "Ami/groups_detail.html", context)

	def post(self, request, slug):
		group = Group.objects.get(slug=slug)
		user = request.user
		if 'join' in request.POST:
			add_member = GroupMember(group=group, user=user)
			add_member.save()
			return redirect('view-group', group.slug)
		elif 'leave' in request.POST:
			membership = GroupMember.objects.get(group=group, user=user)
			membership.delete()
			return redirect('view-group', group.slug)
		else:
			print("Invalid Request")
			return redirect('view-group', group.slug)

