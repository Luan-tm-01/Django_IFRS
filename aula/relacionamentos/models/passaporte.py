from datetime import date
from django.db import models
from django.forms import ValidationError
from .pessoa import Pessoa
from relacionamentos.models import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Passaporte(BaseModel):
    numero = models.CharField(max_length=10,
                              unique=True,
                              validators=[MinLengthValidator(4)],
                              verbose_name="Número do passaporte",
                              help_text="Digite o número do passaporte"
                              )
    
    emissao = models.DateField(
        verbose_name="Data de emissão",
        help_text="Selecione a data de emissão do passaporte",
        validators=[MinValueValidator(date.today),MaxValueValidator(date.today)]
    )

    vencimento = models.DateField(
        verbose_name="Vencimento do passaporte",
        help_text= "Selecione a data de vencimento do passaporte"
    )

    # Realiza a associação entre as classes 1:1
    pessoa = models.OneToOneField(Pessoa,
                                  help_text="Selecione o titular do passaporte",
                                  on_delete=models.CASCADE)
    
    def clean(self):
        if self.emissao > self.vencimento:
            raise ValidationError({
                'emissao': "Data não pode ser posterior ao vencimento",
                'vencimento': "Data não pode ser anterior a emissão"
            })
        
        elif self.pessoa.data_nascimento > self.emissao:
            raise ValidationError({
                "emissao": "Data de emissão não pode ser anterior ao nascimento do titular"
            })
        
    def __str__(self):
        return f'{self.numero} - {self.pessoa}'