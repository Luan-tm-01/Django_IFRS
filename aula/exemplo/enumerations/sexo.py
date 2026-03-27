from django.db import models

class Sexo(models.TextChoices):
    FEMININO = "F", "Feminino"
    MASCULINO = "M", "Masculino"
