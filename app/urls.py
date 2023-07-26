from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario),
    path('preguntas/', views.preguntas),
    path('a/b/c/d/template/', views.preguntas_con_template),
]
