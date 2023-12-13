from .models import Reserva
from django import forms


class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva

        fields = ["nombre", "apellido", "fecha", "hora", "tipo_evento"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha": forms.DateInput(attrs={'class': 'form-control'}),
            "hora": forms.TimeInput(attrs={'class': 'form-control'}),
            "tipo_evento": forms.TextInput(attrs={'class': 'form-control'}),
            
                }
        