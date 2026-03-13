from django.contrib import admin
from .models import Pessoa, Passaporte, Reporter, Artigo, ArtigoAdmin, Revista, Reportagem

admin.site.register(Pessoa)
admin.site.register(Passaporte)
admin.site.register(Reporter)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Revista)
admin.site.register(Reportagem)

