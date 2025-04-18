from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        preco = request.POST.get('preco', 0)
        quantidade = request.POST.get('quantidade', 0)

        # Validação básica dos campos
        if nome and descricao and preco and quantidade:
            Produto.objects.create(nome=nome, descricao=descricao, preco=float(preco), quantidade=int(quantidade))
            return redirect('listar_produtos')  # Redireciona após sucesso
        else:
            return render(request, 'produtos/adicionar.html', {'error': 'Preencha todos os campos corretamente!'})

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

from django.shortcuts import render, redirect

def listar_produtos(request):
    return render(request, 'produtos/listar.html')

def adicionar_produto(request):
    return render(request, 'produtos/adicionar.html')

from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)