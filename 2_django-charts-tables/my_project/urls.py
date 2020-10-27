
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^', include('my_apps.user_auth.urls')),
    url(r'^', include('my_apps.chart_app.urls'))
]
