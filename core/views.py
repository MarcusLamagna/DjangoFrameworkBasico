from django.shortcuts import render

from .models import Product


# Criando a função index que recebe um parametro request
def index(request):
    produtos = Product.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def produto(request, pk):
    prod = Product.objects.get(id=pk)

    context = {
        'product': prod
    }
    return render(request, 'produto.html', context)
