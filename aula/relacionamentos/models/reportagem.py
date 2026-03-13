from datetime import date
from .revista import *
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import *

class Reportagem(BaseModel):
    titulo = models.CharField(max_length=200,
                              validators=[MinLengthValidator(3)],
                              verbose_name="Título",
                              help_text="Insira o título da reportagem")
    
    publicacao = models.DateField(verbose_name="Publicação",
                                  validators=[
                                      MinValueValidator(date.today)
                                  ],
                                  help_text="Insira a data da publicação")
    #Field para o relacionamento N:N simples
    revistas = models.ManyToManyField(Revista,
                                      help_text="Selecione as revistas nas quais a reportagem foi publicada")
    
    class Meta:
        verbose_name_plural = "Reportagens"