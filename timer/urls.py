from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'timer'

urlpatterns = [
    url(r'^$', views.timefetch, name='timefetch'),
]