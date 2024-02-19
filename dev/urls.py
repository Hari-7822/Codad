
from django.urls import path
from alpha import settings

from . import views

urlpatterns = [
    path('', views.co, name = "index"),
]
