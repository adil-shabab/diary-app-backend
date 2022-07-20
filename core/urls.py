from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/update/<str:pk>/', views.updateNote, name='update'),
    path('notes/create/', views.createNote, name='create'),
    path('notes/<str:pk>/', views.getNote, name='note'),
    path('notes/delete/<str:pk>/', views.deleteNote, name='delete'),
]