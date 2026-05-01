from django.contrib import admin
from django.urls import path, include
from .views.estaticas import index

urlpatterns = [
    path('', index, name="index" ),
    path('admin/', admin.site.urls),
    path('basico/', include("basico.urls", namespace="basico")),
    path('relacionamentos/', include("relacionamentos.urls", namespace="relacionamentos")),
]
