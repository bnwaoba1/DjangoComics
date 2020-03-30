from django.urls import path, include   #copied from project urls.py
from . import views


urlpatterns = [
    path('', views.home),
]