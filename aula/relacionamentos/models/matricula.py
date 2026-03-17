from datetime import date
from django.db import models
from relacionamentos.models import BaseModel, Aluno, Disciplina
from django.core.validators import MinValueValidator, MaxValueValidator
from relacionamentos.enumerations import Status

class Matricula(BaseModel):
    data = models.DateField(help_text="Insira a data da matrícula")
    nota = models.FloatField(help_text="Nota final do aluno",
                             validators=[MinValueValidator(0.0),
                                         MaxValueValidator(10.0)])
    frequencia = models.FloatField(verbose_name="Frequência",
                                   help_text="Informe a frequência final do aluno")
    status = models.CharField(max_length=20, 
                              help_text="Status do aluno para a matrícula",
                              default=Status.MATRICULADO,
                              choices=Status)
    
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT,
                              help_text="Selecione o aluno para a matrícula")
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT,
                                   help_text="Selecione a disciplina para o aluno")

    def __str__(self):
        return f"{self.data} - {self.aluno.nome} - {self.disciplina.nome}"

    #Salvar a data atual de acordo com a nota e frequencia