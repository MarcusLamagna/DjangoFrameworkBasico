from django.shortcuts import render


# Criando a função index que recebe um parametro request
def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
