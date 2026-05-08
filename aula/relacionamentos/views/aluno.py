from django.shortcuts import render, get_object_or_404, redirect
from relacionamentos.models import Aluno
from django.views import View

class AlunoListarView(View):
    @staticmethod
    def get(request):
        alunos = Aluno.objects.all()
        contexto = {
        'alunos': alunos
        }

        return render(request, "aluno/listar.html", contexto)

class AlunoLerView(View):
    @staticmethod
    def get(request, id):
        aluno = Aluno.objects.get(id=id)
        contexto = {
            "aluno": aluno
        }

        return render(request, "aluno/ler.html", contexto)
    
class AlunoDeletarView(View):
    @staticmethod
    def get(request, id):
        aluno = get_object_or_404(Aluno,id=id)
        try:
            contexto = {
                'aluno' : aluno
            }
            return render(request,'aluno/deletar.html',contexto)
        
        except Exception as e:
            contexto = {}
            print(e)
            return render(request,'aluno/listar.html',contexto)
        
    @staticmethod
    def post(request, id):
        aluno = get_object_or_404(Aluno, id=id)
        try:
            aluno_id_form = request.POST.get("aluno_id", None)
            if int(aluno_id_form) == id:
                aluno.delete()
                # Fazer Mensagens
                return redirect("relacionamentos:classe_aluno_listar")
        except Exception as e:
            print(e)
            # Adicionar Mensagens
            contexto = { }
            return render (request, "aluno/listar.html", contexto)

