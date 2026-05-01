from django.shortcuts import render
from relacionamentos.models import Aluno


def listar(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos
    }

    return render(request, "aluno/listar.html", contexto)

def ler(request, id):
    aluno = Aluno.objects.get(id=id)
    contexto = {
        "aluno": aluno
    }

    return render(request, "aluno/ler.html", contexto)