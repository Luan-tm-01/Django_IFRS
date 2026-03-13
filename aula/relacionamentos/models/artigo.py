from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError
from .base_model import *
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date
from .reporter import Reporter

class Artigo(BaseModel):
    titulo = models.CharField(max_length=255,
                              validators=[MinLengthValidator(5)],
                              verbose_name='Título',
                              help_text="Título do artigo")
    publicacao = models.DateField(verbose_name="Publicação",
                                  help_text="Selecione a data da publicação",
                                  validators=[MinValueValidator(date.today)])
    
    # Tipo de field que permite a relação de associação 1:N ou N:1
    reporter = models.ForeignKey(Reporter, verbose_name="Reporter Autor",
                                 help_text="Selecione o autor do artigo",
                                 on_delete=models.CASCADE)

    def clean(self):
        data_publicacao = self.publicacao
        data_publicacao = data_publicacao.replace(year=data_publicacao.year - 18)

        if  self.reporter.data_nascimento > data_publicacao:
            raise ValidationError({
                'publicacao': "Reporter não possui idade mínima para publicar"
            })
        
    def __str__(self):
        return self.titulo
    
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo','publicacao', 'reporter')
    search_display = ('titulo', 'publicacao')
    list_filter = ('publicacao',)