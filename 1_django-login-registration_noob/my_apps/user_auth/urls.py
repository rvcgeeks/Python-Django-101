
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
]
