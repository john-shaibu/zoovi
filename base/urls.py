from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='home'),
      path('auth/login/', views.loginPage, name='login'),
      path('auth/register/', views.registerPage, name='register'),
      path('dashboard/', views.dashboard, name='dashboard'),
]

