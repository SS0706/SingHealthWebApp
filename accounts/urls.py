from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stores/', views.stores, name='stores'),
    path('report/', views.report, name='report'),
    path('announcements/', views.announcements, name='announcements'),
]