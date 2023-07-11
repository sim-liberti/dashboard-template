from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user-login'),
    path('signup/', views.signup_view, name='user-signup'),
    path('logout/', views.logout_view, name='user-logout'),
    path('profile/', views.profile_view, name='user-profile'),
]