from django.db import models
from exemplo.models import BaseModel

class Categoria(BaseModel):
    nome = models.CharField(max_length=20)
    area = models.CharField(max_length=20, null=True, blank=True, verbose_name='Area do conhecimento', help_text='Informe a area de conhecimento')
    instituicao = models.CharField(max_length=10, default='IFRS')

    def __str__(self):
        return f'{self.id} : {self.nome}  {self.area} {self.instituicao}'