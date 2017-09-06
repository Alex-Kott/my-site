from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils import timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

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
		user = Users.objects.get(login = login)
		context['error'] = 'user_exist'
		return render(request, 'polls/error.html', context)
	except:
		try:
			u = Users(login = form['login'], password = form['password'], date = timezone.now())
			u.save()
			# test_django_app:qazwsx123
			if is_email(form['login']):
				send_mail(request)
		except Exception as e:
			print(str(e))
	return redirect("/")

def send_mail(request):
	print(request)
	form = request.POST
	fromaddr = "test_django_app@mail.ru"
	toaddr = form['login']
	mypass = "qazwsx123"
	 
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Регистрация"
	 
	body = "Вы зарегистрировались в нашем блоге. Ваш пароль: {}".format(form['password'])
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.mail.ru', 587)
	server.starttls()
	server.login(fromaddr, mypass)
	text = msg.as_string()
	try:
		server.sendmail(fromaddr, toaddr, text)
	except:
		print("Mail send error")
	server.quit()

def is_email(email):
	flag = re.findall(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', email)
	if len(flag) == 1:
		return True
	else:
		return False

def auth(request):
	form = request.POST
	login = form['login']
	password = form['password']
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

def remove(request):
	data = request.POST
	post_id = data['post']
	Posts.remove(post_id)
	return JsonResponse({})
