from .base_model import *
from django.core.validators import MinLengthValidator

class Esporte(BaseModel):
    nome = models.CharField(max_length=20,
                            validators=[MinLengthValidator(4)],
                            help_text="Nome para do esporte")
    
    def __str__(self):
        return f'{self.nome}'