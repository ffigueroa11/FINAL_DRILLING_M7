from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_list, name='laboratorio_list'),
    path('create/', views.laboratorio_create, name='laboratorio_create'),
    path('edit/<int:pk>/', views.laboratorio_edit, name='laboratorio_edit'),
    path('delete/<int:pk>/', views.laboratorio_delete, name='laboratorio_delete'),
    path('laboratorio/<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'),
]