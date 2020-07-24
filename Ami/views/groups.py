from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from Ami.models import Group

class Groups(View):
    def get(self, request):
        all_groups = Group.objects.all()
        context = {'groups': all_groups}
        return render(request, "Ami/groups_list.html", context)
    
