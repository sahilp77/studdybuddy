from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.Members , name='members')
]