from basico.views import PrimeiraView, SaudacaoView, SaudacaoNomeView, AlterarSenhaView, OperacaoCalculoView, CompetidorRead
from django.urls import path
import basico.views.funcoes as views
from basico.views import read_competidor, list_competidores


app_name = "basico"

urlpatterns = [
    path("funcao/primeira", views.funcao_primeira, name='funcao_primeira'),
    path("funcao/saudacao", views.saudacao, name="saudacao"),
    path("funcao/saudacao_nome/<str:nome>", views.saudacao_nome, name="saudacao_nome"),
    path("funcao/alterar_senha/<str:senha>", views.alterar_senha, name="alterar_senha"),
    path("funcao/<str:operacao>/<int:valor1>/<int:valor2>", views.operacao_calculo),
    path("classe/primeira", PrimeiraView.as_view(), name="classe_primeira"),
    path("classe/saudacao", SaudacaoView.as_view(), name="saudacao"),
    path("classe/saudacao_nome/<str:nome>", SaudacaoNomeView.as_view(), name="saudacao_nome"),
    path("classe/alterar_senha/<str:senha>", AlterarSenhaView.as_view(), name="alterar_senha"),
    path("classe/<str:operacao>/<int:valor1>/<int:valor2>", OperacaoCalculoView.as_view()),
    path("competidor/funcao/<int:id>", read_competidor, name="read_competidor"),
    path("competidor/classe/<int:id>", CompetidorRead.as_view(), name="classe_competidor_read"),
    path("competidor/funcao", list_competidores, name = "funcao_list_competidores")
]