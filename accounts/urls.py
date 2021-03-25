from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='accounts.login'),
    path('register', views.register, name='accounts.register'),
    path('logout', views.logout, name='accounts.logout'),
    path('dashboard', views.dashboard, name='accounts.dashboard'),
]
