from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    pass

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=999)
    slug = models.SlugField(allow_unicode=True, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('view-group', args=[str(self.slug)])

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_group', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'user')