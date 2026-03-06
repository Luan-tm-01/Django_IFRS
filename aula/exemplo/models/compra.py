from django.db import models
from exemplo.models import BaseModel

class Compra(BaseModel):
    data = models.DateField() 
    hora = models.TimeField() 
    valor = models.DecimalField(max_digits=6, decimal_places=2) 
    quantidade_de_itens = models.IntegerField() 
    peso = models.FloatField()
    descricao = models.TextField(verbose_name='Descrição') 
    cliente = models.CharField(verbose_name='Nome do Cliente',max_length=100)
    cpf = models.CharField(verbose_name='CPF', max_length=11)

    def __str__(self):
        return f"{self.cliente} : {self.data}"
