from relacionamentos.forms import Baseform
from relacionamentos.models import Pessoa

class PessoaForm(Baseform):
    class Meta:
        model = Pessoa
        fields = "__all__"

