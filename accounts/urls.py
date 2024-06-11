from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.signup, name = 'register'),
    
    path('login/', views.login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/view/', views.view_profile, name='view_profile'),
    
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

