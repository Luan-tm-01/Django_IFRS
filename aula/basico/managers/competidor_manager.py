from django.db.models import QuerySet
from basico.managers import BaseManager

class CompetidorManager(BaseManager):
    def find_by_nome(self, nome:str) -> QuerySet['Competidor']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(nome__icontains=nome)
            return consulta
        else:
            raise TypeError('O nome deve ser string')