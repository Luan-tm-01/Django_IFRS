from .base_model import *
from django.core.validators import MinLengthValidator

class Time(BaseModel):
    nome = models.CharField(max_length=20,
                            validators=[MinLengthValidator(3)],
                            help_text="Nome para o time")
    
    def __str__(self):
        return f'{self.nome}'