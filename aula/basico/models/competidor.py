from django.core.validators import MinLengthValidator
from django.db import models
from basico.models import BaseModel
from basico.managers import CompetidorManager

class Competidor(BaseModel):
    nome = models.CharField(max_length=200,
                            validators=[MinLengthValidator(3)])
    
    objects = CompetidorManager()
    
    def __str__(self):
        return self.nome