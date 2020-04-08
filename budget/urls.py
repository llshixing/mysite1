from django.urls import path

from . import views

urlpatterns = [
    path('payment/budgetlist/', views.budgetlist, name='budgetlist'),
]