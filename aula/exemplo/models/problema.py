from django.db import models
from exemplo.models import BaseModel
from exemplo.enumerations import Nivel
from exemplo.validators import ValidarTamanhhoMemoria
from exemplo.validators import PalavrasProibidas
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator

class Problema(BaseModel):

    cod = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(1000)],
        help_text='Código do problema',
        verbose_name='Código'
    )

    titulo = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3),
                    PalavrasProibidas(
                        lista_proibida=["teste", "admin"],
                        mensagem="O campo contém palavras que foram proibidas. Ex: teste, admin"
                    )],
        help_text='Título do problema',
        verbose_name='Título'
    )

    nivel = models.IntegerField(
        choices=Nivel,
        default=Nivel.UM,
        verbose_name='Nível',
        help_text="Escolha o nível do problema"
    )

    descricao = models.TextField(
        max_length=2000,
        validators=[MinLengthValidator(20),
                    PalavrasProibidas(
                        lista_proibida=["irã", "trump", "eua"],
                        mensagem="Você utilizou palavras proibidas. Revise as diretrizes das questões."
                    )],
        verbose_name="Descrição",
        help_text="Insira a descrição do problema para o usuário"
    )

    exemplo_entrada = models.TextField(
        max_length=2000,
        verbose_name="Exemplo de entrada",
        help_text="Entrada para a solução do problema"
    )

    exemplo_saida = models.TextField(
        max_length=2000,
        validators=[MinLengthValidator(1)],
        verbose_name="Saída esperada",
        help_text="Saída esperada para a solução do problema"
    )

    pontuacao = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name="Pontuação",
        help_text="Insira a pontuação a ser creditada para o usuário"
    )

    tempo_execucao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        verbose_name="Tempo de execução do programa",
        help_text="Insira o tempo máximo de execução"
    )

    memoria_maxima = models.IntegerField(
        validators=[MinValueValidator(8), MaxValueValidator(256), ValidarTamanhhoMemoria],
        verbose_name="Memória Máxima",
        help_text="Informe a quantidade em MB de memória a ser utilizada"
    )

    resolvidos = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Resolvido",
        default=0,
        help_text="Quantidade de usuários que resolveram o problema"
    )

    def __str__(self):
        return f"{self.titulo} : {self.pontuacao}"