from django.contrib import admin
from .models import Reserva
# Register your models here.
class Reserva_tarea(admin.ModelAdmin):
    readonly_fields=("creado", )


admin.site.register(Reserva, Reserva_tarea)

    