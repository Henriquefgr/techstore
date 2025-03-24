from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),  # Adicionar produto

]
from django.shortcuts import render, redirect
from .forms import ProdutoForm

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona após adicionar
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar.html', {'form': form})