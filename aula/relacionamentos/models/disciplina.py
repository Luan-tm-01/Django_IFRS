from django.db import models
from relacionamentos.models import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Disciplina(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)],
                            help_text="Nome da Disciplina")
    
    sigla = models.CharField(max_length=5,
                             validators=[MinLengthValidator(3)],
                             help_text="Sigla da Disciplina")
    
    semestre = models.IntegerField(validators=[MinValueValidator(1),
                                   MaxValueValidator(10)],
                                   help_text="Semestre da Disciplina")
    
    ementa = models.TextField(help_text="Ementa da Disciplina")