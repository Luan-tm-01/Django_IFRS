from django.shortcuts import render
from relacionamentos.models import Pessoa


def listar(request):
    pessoas = Pessoa.objects.all()
    contexto = {
        'pessoas': pessoas
    }

    return render(request, "pessoa/listar.html", contexto)

def ler(request, id):
    pessoa = Pessoa.objects.get(id=id)
    contexto = {
        "pessoa": pessoa
    }

    return render(request, "pessoa/ler.html", contexto)