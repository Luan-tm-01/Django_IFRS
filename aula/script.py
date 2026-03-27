from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

#"Abriu" o shell

from relacionamentos.models import Pessoa, Aluno, Disciplina, Matricula
from relacionamentos.enumerations import Status


luan = Pessoa(
    nome = "Luan Teixeira",
    data_nascimento = "2005-04-06",
    cpf = 11111111111
)

luan.full_clean()
luan.save()

aluno_1 = Aluno(
    nome = "Aluno 1",
    data_nascimento = "2000-04-06",
    cpf = 22222222522,
    email = "aluno1@email.com",
    cod = 1111111111
)

aluno_1.full_clean()
aluno_1.save()

disciplina_2 = Disciplina(
    nome = "Disciplina 2",
    sigla = "DIS 2",
    semestre = 2,
    ementa = "cfguyacnvae"

)

disciplina_2.full_clean()
disciplina_2.save()

matricula_3 = Matricula(
    data = "2025-02-03",    
    nota = 5,
    frequencia = 75,
    status =  Status.MATRICULADO,
    aluno = aluno_1,
    disciplina = disciplina_2
)

matricula_3.full_clean()
matricula_3.save()