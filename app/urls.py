from django.urls import path
from app import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('calculator', views.calculator, name='calculator'),
    path('history/', views.history, name='history'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
