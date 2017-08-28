from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Posts

def index(request):
	form = request.POST
	try:
		p = Posts(post_text = form['txt'], author = form['username'], date = timezone.now())
		p.save()
	except:
		print("Posts doesn't exist")
	posts = Posts.objects.all()
	print(posts)
	context = { 'posts' : posts}
	return render(request, 'polls/index.html', context)

