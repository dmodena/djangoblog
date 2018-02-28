from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('lista-todos/', views.lista, name='lista_todos'),
    path('novo/', views.novo),
    path('atualizar/<int:id>', views.atualiza, name='atualizar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
