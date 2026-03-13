from django.db import models
from .pessoa import Pessoa
from django.core.validators import MinLengthValidator

class Reporter(Pessoa):

    email = models.EmailField(max_length=100,
                              validators=[MinLengthValidator(5)],
                              verbose_name="E-mail",
                              help_text="Insira o e-mail institucional",)
    