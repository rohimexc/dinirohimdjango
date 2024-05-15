
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
     path('', views.index, name='index'),

     path('data-undangan', views.data_undangan, name='data-undangan'),
]