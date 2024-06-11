from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_list_new, name='quiz_list_new'),
    
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    
    path('result/', views.quiz_result, name='quiz_result'),
    
    path('progress/', views.user_progress, name='user_progress'),
    
    path('leaderboard/', views.leaderboards, name='leaderboards'),
    
    path('category/', views.category_list, name='category_list'),
    
    path('<int:quiz_id>/rate/', views.rate_quiz, name='rate_quiz'),
]
