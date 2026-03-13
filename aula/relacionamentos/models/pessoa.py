from datetime import date
from django.forms import ValidationError
from relacionamentos.validators.validador_cpf import validacao_cpf
from .base_model import *
from django.core.validators import MinLengthValidator, MaxValueValidator

class Pessoa(BaseModel):
    nome = models.CharField(max_length=100,
                            help_text="Nome da pessoa",
                            validators=[MinLengthValidator(5)])
    data_nascimento = models.DateField(verbose_name="Data de Nascimento",
                                       help_text="Selecione a data de Nascimento",
                                       validators=[MaxValueValidator(date.today)])
    cpf = models.CharField(max_length=11, unique=True,
                           validators=[MinLengthValidator(11),
                                       validacao_cpf,],
                                       help_text="Insira um CPF válido",
                                       verbose_name="CPF")
    
    def clean(self):
        hoje = date.today()
        if self.data_nascimento > hoje:
            raise ValidationError({
                'data_nascimento': "Não é possível cadastrar pessoas que ainda não nasceram"
            })
        
    def __str__(self):
        return self.nome