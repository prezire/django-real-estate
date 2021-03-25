from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings.index'),
    path('<int:id>', views.read, name='listings.read'),
    path('search', views.search, name='listings.search'),
]
