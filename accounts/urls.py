from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stores/', views.stores, name='stores'),
    path('report/', views.report, name='report'),
    path('announcements/', views.announcements, name='announcements'),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # forms
    path('createReport_form/', views.createReport, name='createReport_form'),
    path('rectify_form/', views.createRectification, name='rectify_form'),

]
