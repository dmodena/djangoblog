from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('lista-todos/', views.lista),
    path('novo/', views.novo),
]
