from django.urls import path

from . import views

urlpatterns = [
    path('', views.userLogin, name='userLogin'),
]