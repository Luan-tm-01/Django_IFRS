from django.http import HttpResponse, Http404
from datetime import datetime


def funcao_primeira(request):
    mensagem = "Hello World!"
    return HttpResponse(mensagem, status=200)


def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa Noite!"
    if 6 >= agora.hour < 12:
        mensagem = "Bom Dia!"
    elif 12 <= agora.hour < 18:
        mensagem = "Boa Tarde!"
    elif 18 <= agora.hour < 24:
        mensagem = "Boa Noite!"
    else:
        mensagem = "Boa Madrugada!"
    
    saida = (f"<html><body><h1>{mensagem.upper()}</h1>"
            f"<br/> {agora}"
            f"<br/> {request.META["REMOTE_ADDR"]}"
            f"</body></html>")

    return HttpResponse(saida, status=200)

def saudacao_nome(request, nome):
    mensagem = f"Olá {nome.title()}"
    return HttpResponse(mensagem, status=200)

def alterar_senha(request, senha):
    senha_alterada = senha.replace("a","4")
    senha_alterada = senha_alterada.replace("e","3")
    senha_alterada = senha_alterada.replace("i","1") 
    senha_alterada = senha_alterada.replace("o","0")
    senha_alterada = senha_alterada.replace("u","v")
    senha_alterada = senha_alterada.replace("p","b")
    mensagem = f"Sua senha alterada ficou: {senha_alterada}"
    return HttpResponse(mensagem, status=200)

def operacao_calculo(request, operacao, valor1, valor2):
    if operacao.upper() == "ADICAO":
        resultado = valor1 + valor2
    elif operacao.upper() == "SUBTRACAO":
        resultado = valor1 - valor2
    elif operacao.upper() == "MULTIPLICACAO":
        resultado = valor1 * valor2
    elif operacao.upper() == "DIVISAO":
        resultado = valor1 / valor2
    elif operacao.upper() == "RESTO":
        resultado = valor1 % valor2
    elif operacao.upper() == "DIVISAO_INTEIRO":
        resultado = valor1 // valor2
    else:
        raise Http404 ("Error 404")
    operacao = operacao.title()
    mensagem = f"Operação: {operacao} <br/> Resultado:{resultado}"
    return HttpResponse(mensagem, status=200)