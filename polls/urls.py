from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^add_post/$', views.add_post, name = 'add_post'),
	url(r'^sign-up/$', views.signup, name = 'sign_up'),
	url(r'^auth/$', views.auth, name = 'auth'),
]