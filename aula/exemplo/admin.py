from django.contrib import admin
from exemplo.models import Categoria
from exemplo.models import Compra
from exemplo.models import Problema

admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Problema)
