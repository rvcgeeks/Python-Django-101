
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.urls import path
from .views import *

urlpatterns = [
    path('chart_app', render_all_charts, name='chart_app'),
    path('tick_update', update_charts, name='tick_update')
]
