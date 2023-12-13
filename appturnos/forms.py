from django.forms import ModelForm
from .models import Reserva


class FormReserva(ModelForm):
    class Meta:
        model = Reserva

        fields = ['nombre', 'apellido','fecha', 'hora', 'tipo_evento']