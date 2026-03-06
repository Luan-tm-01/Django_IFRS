from django.db import models

class Profissao(models.TextChoices):
    #CONSTANTE = "Nome do Banco", "Nome para Usuario"
    ANALISTA = "Analista", "Analista de Sistemas"
    DESEMPREGADO = "Desempregado", "Desempregado"
    ESTUDANTE = "Estudante", "Estudante"
    PROGRAMADOR = "Programador", "Programador"
    PROFESSOR = "Professor", "Professor"

