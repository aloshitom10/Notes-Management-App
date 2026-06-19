from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_note/', views.create_note, name='create_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
    path('logout/', views.logout_user, name='logout'),
]