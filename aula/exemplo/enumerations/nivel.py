from django.db import models

class Nivel(models.IntegerChoices):
    UM = 1, "1"
    DOIS = 2, "2"
    TRES = 3, "3"
    QUATRO = 4, "4"
    CINCO = 5, "5"
    SEIS = 6, "6"
    SETE = 7, "7"
    OITO = 8, "8"
    NOVE = 9, "9"
    DEZ = 10, "10"
