from django.urls import path
from relacionamentos.views import *


app_name = "relacionamentos"

urlpatterns = [
   path("pessoa/funcao/ler/<int:id>/", pessoa.ler, name="funcao_pessoa_ler"),
   path("pessoa/funcao/listar/", pessoa.listar, name="funcao_pessoa_listar"),
   path("pessoa/funcao/deletar/<int:id>/", pessoa.deletar, name="funcao_pessoa_deletar"),
   path("pessoa/funcao/criar/", pessoa.criar, name="funcao_pessoa_criar"),
   path("pessoa/funcao/editar/<int:id>/", pessoa.editar, name="funcao_pessoa_editar"),


   
   path("aluno/classe/ler/<int:id>/", AlunoLerView.as_view(), name="classe_aluno_ler"),
   path("aluno/classe/listar/", AlunoListarView.as_view(), name="classe_aluno_listar"),
   path("aluno/classe/deletar/<int:id>/", AlunoDeletarView.as_view(), name="classe_aluno_deletar"),
   
]