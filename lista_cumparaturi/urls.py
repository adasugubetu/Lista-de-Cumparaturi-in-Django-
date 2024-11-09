from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adauga/', views.adauga_produs, name='adauga_produs'),
    path('sterge/<int:produs_id>/', views.sterge_produs, name='sterge_produs'),
    path('marcheaza/<int:produs_id>/', views.marcheaza_cumparat, name='marcheaza_cumparat')
]
