from django.urls import path
from . import views  # Importando views corretamente

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),  # Página inicial - Listar produtos
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),  # Adicionar produto
]
