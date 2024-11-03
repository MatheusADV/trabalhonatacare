from django.contrib import admin
from .models import usuario, clinica, endereco

# Register your models here.
admin.site.register(usuario)
admin.site.register(clinica)
admin.site.register(endereco)
