from django.urls import path
from relacionamentos.views import *


app_name = "relacionamentos"

urlpatterns = [
   path("pessoa/funcao/ler/<int:id>/", pessoa.ler, name="funcao_pessoa_ler"),
   path("pessoa/funcao/listar/", pessoa.listar, name="funcao_pessoa_listar"),
   path("aluno/funcao/ler/<int:id>/", aluno.ler, name="funcao_aluno_ler"),
   path("aluno/funcao/listar/", aluno.listar, name="funcao_aluno_listar"),
]