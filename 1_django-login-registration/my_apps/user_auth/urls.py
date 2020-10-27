
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin', admin.site.urls),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout, name='mylogout')
]
