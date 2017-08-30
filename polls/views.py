from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone


from .models import Posts
from .models import Users

def index(request):
	
	posts = Posts.objects.all()
	context = { 'posts' : posts}
	return render(request, 'polls/index.html', context)

def add_post(request):
	form = request.POST
	print(form)
	try:
		p = Posts(post_text = form['txt'], author = form['user'], date = timezone.now())
		p.save()
	except:
		print("Posts doesn't exist")	
	return redirect("/")

def signup(request):
	form = request.POST
	print(form)
	try:
		u = Users(login = form['login'], password = form['password'], date = timezone.now())
		u.save()
	except:
		print("User registration error")
	return redirect("/")

def auth(request):
	form = request.POST
	login = form['login']
	password = form['password']
	print(login)
	context = {}
	try:

		user = Users.objects.get(login = login)
	except Users.DoesNotExist:

		context['user'] = login
		context['error'] = 'user_not_found'
		return render(request, 'polls/error.html', context)

	if user.password != password:
		context['error'] = 'wrong_password'
		return render(request, 'polls/error.html', context)
	
	return redirect("/")