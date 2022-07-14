from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.index, name='index'),
    path('search/not_found/', views.not_found, name='not_found'),
]