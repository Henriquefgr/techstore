from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    # Adicione outras rotas aqui, como adicionar, editar e excluir produtos.
]
from django.shortcuts import render

def listar_produtos(request):
    return render(request, 'produtos/listar.html')