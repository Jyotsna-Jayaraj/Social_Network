"""Social_Network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Ami.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('create-group', CreateGroup.as_view(), name='create-group'),
    path('groups', Groups.as_view(), name='groups'),
    path('group/<slug:slug>', ViewGroup.as_view(), name='view-group'),
    path('create-post', CreatePost.as_view(), name='create-post'),
]
