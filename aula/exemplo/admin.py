from django.contrib import admin
from exemplo.models import Categoria
from exemplo.models import Compra
from exemplo.models import Problema
from exemplo.models import Time
from exemplo.models import Esporte
from exemplo.models import Cidade
from exemplo.models import Pessoa

admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Problema)
admin.site.register(Time)
admin.site.register(Esporte)
admin.site.register(Cidade)
admin.site.register(Pessoa)
