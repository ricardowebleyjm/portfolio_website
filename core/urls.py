from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.SaveEmailView.as_view(), name='subscribe'),
    path('hire-me/', views.HireMe.as_view(), name='hire_me'),
]