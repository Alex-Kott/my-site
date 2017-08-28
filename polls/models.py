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
