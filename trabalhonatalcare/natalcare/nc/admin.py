from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(usuario)
admin.site.register(clinica)
admin.site.register(endereco)
admin.site.register(especialidades)
admin.site.register(plano)
admin.site.register(comentario)
admin.site.register(historico)