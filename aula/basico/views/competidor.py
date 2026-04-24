from django.http import HttpResponse, JsonResponse
from basico.models import Competidor
from django.core import serializers
from django.views import View
from django.shortcuts import render

def read_competidor(request, id:int):
    competidor = Competidor.objects.get(pk=id)

    tipo = request.GET.get('tipo', "")

    match tipo.lower():
        case "http":
            saida = (f"<p><b>ID: {competidor.id} </b></p>"
                    f"<p><b>Nome: {competidor.nome}</b></p>")
            return HttpResponse(saida, status=200)
        case "json":
            objeto = serializers.serialize("json", [competidor])
            return JsonResponse(objeto, safe=False)
        case _:
            saida = "Bad Request"
            return HttpResponse(saida, status=400)
        

def list_competidores(request):
    nome = request.GET.get('nome', None)

    if nome != None:
        competidores = Competidor.objects.find_by_nome(nome)
    else:
        competidores = Competidor.objects.all()

    contexto = {
        "mensagem": "Bem-vindo(a) a aula de Dev1"
    }
    saida = ""
    for competidor in competidores:
        saida += f"<p><b>ID: {competidor.id} </b></p>"
        saida += f"<p><b>Nome: {competidor.nome}</b></p>"
        saida += f"<hr>"

    return render(request, "competidor.html", contexto)
        
class CompetidorRead(View):
    @staticmethod
    def get(request, id:int):
        competidor = Competidor.objects.get(pk=id)

        tipo = request.GET.get('tipo', "")

        match tipo.lower():
            case "http":
                saida = (f"<p><b>ID: {competidor.id} </b></p>"
                        f"<p><b>Nome: {competidor.nome}</b></p>")
                return HttpResponse(saida, status=200)
            case "json":
                objeto = serializers.serialize("json", [competidor])
                return JsonResponse(objeto, safe=False)
            case _:
                saida = "Bad Request"
                return HttpResponse(saida, status=400)