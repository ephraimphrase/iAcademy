from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signOut/', views.signOut, name='signOut'),
    path('registerStudent/', views.registerStudent, name='register-student'),
    path('editStudent/<str:pk>/', views.editStudent, name='edit-student'),
    path('deleteStudent/<str:pk>/', views.deleteStudent, name='delete-student')
]
