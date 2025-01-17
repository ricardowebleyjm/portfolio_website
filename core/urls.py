from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.save_email, name='subscribe'),
]