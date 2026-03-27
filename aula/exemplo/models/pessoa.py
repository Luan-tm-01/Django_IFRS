from .base_model import *
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from exemplo.enumerations import Sexo
from exemplo.models import Time, Cidade, Esporte

class Pessoa(BaseModel):
    nome = models.CharField(max_length=40,
                            validators=[MinLengthValidator(3)],
                            help_text="Nome da Pessoa")
    sexo = models.CharField(max_length=1,
                            validators=[MinLengthValidator(1)],
                            choices=Sexo,
                            help_text="Selecione o Sexo")
    idade = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(200)],
                                help_text="Insira a Idade")
    renda = models.DecimalField(max_digits=10,decimal_places=2,
                                validators=[MinValueValidator(0)],
                                help_text="Adicione a Renda")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE) 


    def __str__(self):
        return f'{self.nome} / {self.time}'