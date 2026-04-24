from django.shortcuts import render

def index(request):
    contexto = {
        "mensagem": "Bem-vindo(a) a aula de Dev1"
    }

    return render(request, "index.html", contexto)