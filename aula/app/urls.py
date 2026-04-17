from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basico/', include("basico.urls", namespace="basico")),
]
