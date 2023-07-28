from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario),
    path('ejecutar/', views.ejecutar),
]
