from django.urls import path
from apps.productos import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('create/', views.create, name = 'create'),
]   