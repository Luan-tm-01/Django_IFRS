from .base_model import *
from django.core.validators import MinLengthValidator

class Cidade(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            help_text="Nome da Cidade")
    estado = models.CharField(max_length=2,
                              validators=[MinLengthValidator(2)],
                              help_text="Insira a sigla do estado")
    def __str__(self):
        return f'{self.nome}/ {self.estado}'