from django.contrib import admin # type: ignore
from .models import Usuario, Libro, Prestamo

# Registrar los modelos para que aparezcan en el panel de administración de Django
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Prestamo)
