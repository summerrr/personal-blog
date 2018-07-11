from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns=[
	path('login',login,{'template_name':'user/login.html'},name='login'),
	path('logout',views.logout_view,name='logout'),
	path('registers',views.registers,name='registers')
	]