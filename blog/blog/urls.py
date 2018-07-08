"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from blogapp.feeds import AllPostsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('blogapp.urls','blogapp'),namespace='blogapp')),
    path('',include(('comments.urls','comments'),namespace='comments')),
    path('all/rss',AllPostsRssFeed(), name='rss'),
    path('search/',include('haystack.urls'))#一定不要写app name和namespace
]
