from django.urls import path
from . import views

urlpattersn = [
    path("", views.home, name="home")
]