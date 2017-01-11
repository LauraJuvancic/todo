from django.conf.urls import url
import datetime

from . import views

app_name = 'todo'
urlpatterns = [
	url(r'^$', views.first, name='first'),
	url(r'^Homepage/', views.index, name='index'),
	url(r'^Home/', views.home, name='home'),
	url(r'^Work/', views.work, name='work'),
	url(r'^Personal/', views.personal, name='personal'),
	url(r'^Travel/', views.travel, name='travel'),
	url(r'^Shopping/', views.shopping, name='shopping'),
	url(r'^Birthday/', views.birthday, name='birthday'),
	url(r'^Cooking/', views.cooking, name='cooking'),
	url(r'^7days/', views.days, name='7days'),
	url(r'^(?P<idt>[0-9]+)/', views.showDetails, name='details'),
	url(r'^update/(?P<idt>[0-9]+)/', views.updateView, name='update'),
	url(r'^delete/(?P<idt>[0-9]+)/', views.deleteView, name='delete'),
	url(r'^complete/(?P<idt>[0-9]+)/', views.completeTask, name='complete'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^user/(?P<idu>[0-9]+)/', views.showUser, name='showUser'),
	url(r'^editprofile/(?P<idu>[0-9]+)/', views.updateUser, name='updateUser'),
	url(r'^logout/', views.logout_user, name='logout'),
]