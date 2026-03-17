from django.contrib import admin
from .models import Pessoa, Passaporte, Reporter, Artigo, ArtigoAdmin, Revista, Reportagem, Aluno, Disciplina, Matricula

admin.site.register(Pessoa)
admin.site.register(Passaporte)
admin.site.register(Reporter)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Revista)
admin.site.register(Reportagem)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Matricula)
