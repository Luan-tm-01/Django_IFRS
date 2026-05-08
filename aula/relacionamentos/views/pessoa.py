from django.shortcuts import render, get_object_or_404, redirect
from relacionamentos.models import Pessoa
from relacionamentos.forms import PessoaForm


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

def deletar(request,id):
    pessoa = get_object_or_404(Pessoa,id=id)
    try:
        if request.method == 'POST':
            confirmacao_pessoa_id = request.POST.get('pessoa_id')
            if int(confirmacao_pessoa_id) == id:
                pessoa.delete()
                return redirect('relacionamentos:funcao_pessoa_listar')
            raise ValueError(f'ID de confirmação e deleção não confere')
        
        else:
            contexto = {
                'pessoa' : pessoa
            }
            return render(request,'pessoa/deletar.html',contexto)
    except Exception as ex:
        #TODO EXIBIR A MENSAGEM DE ERRO
        contexto = {}
        print(ex)
        return render(request,'pessoa/listar.html',contexto)
    
def criar(request):
    # Método get
    if request.method == "GET":
        form = PessoaForm()

    elif request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("relacionamentos:funcao_pessoa_listar")
        
    contexto = {
        "formulario": form
    }

    return render(request, "pessoa/criar.html", contexto)
        
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == "GET":
        formulario = PessoaForm(instance=pessoa)

    elif request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect("relacionamentos:funcao_pessoa_listar")





    contexto = {
        "formulario": formulario,
        "pessoa": pessoa
    }

    return render(request, "pessoa/editar.html", contexto)