import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Posts(models.Model):
	post_text = models.TextField()
	author = models.CharField(max_length = 100)
	date = models.DateTimeField()

	def remove(post):
		p = Posts.objects.get(id = post)
		p.delete()

class Users(models.Model):
	login = models.CharField(max_length = 100, unique = True)
	password = models.CharField(max_length = 100)
	date = models.DateTimeField()