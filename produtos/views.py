from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

from django.shortcuts import render
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        quantidade = request.POST['quantidade']
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        return redirect('listar_produtos')
    return render(request, 'produtos/adicionar.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.quantidade = request.POST['quantidade']
        produto.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/editar.html', {'produto': produto})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')
