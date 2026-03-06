from django.db import models

class Pais(models.TextChoices):
    ARGENTINA = "ARG", "Argentina"
    BRASIL = "BR", "Brasil"
    EUA = "EUA", "Estados Unidos"
    IRA = "IRA", "Irã"
    OUTRO = "OUT", "Outro"
