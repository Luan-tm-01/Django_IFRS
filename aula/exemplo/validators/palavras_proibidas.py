from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


# Permite que os objetos dessa classe sejam serializados e deserializados

@deconstructible
class PalavrasProibidas:

    # Como instanciar os objetos dessa clase
    def __init__(self, lista_proibida: list, mensagem: str): 
        #lista_proibida = ["teste", "safado", "admin"]
        if not isinstance(lista_proibida, list):
            raise TypeError("A variável lista_proibida deve ser do tipo list.")
        elif len(lista_proibida) == 0:
            raise ValueError("A lista de palavras não deve ser vazia.")
        elif not isinstance(mensagem, str):
            raise TypeError("A mensagem deve ser do tipo string.")
        elif mensagem.strip() == "":
            raise ValueError("A mensagem para o usuário não deve ser vazia")
        
        self.lista_proibida = lista_proibida
        self.mensagem = mensagem
        
    # O que será executado quando for invocado
    def __call__(self, valor_campo):
        for palavra in self.lista_proibida:
            if palavra.lower() in valor_campo.lower():
                raise ValidationError(
                    self.mensagem,
                    params={"value": valor_campo},
                )
        
    # Como determinar se objeto é igual a outro
    def __eq__(self, outro):
        if isinstance(outro, PalavrasProibidas):
            # deve possuir o mesmo tamanho
            if len(self.lista_proibida) == len(outro.lista_proibida):
                for palavra in self.lista_proibida:
                    # se não conter uma determinada palavra
                    if palavra not in outro.lista_proibida:
                        return False
                # mesmo tipo, mesmo tamanho, mesmas palavras, independente
                return True
        return False