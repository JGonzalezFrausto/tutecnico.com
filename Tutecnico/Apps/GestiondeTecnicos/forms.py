from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):  
    class Meta:
        model = Tecnico
        fields = ['ApellidoPaterno', 'ApellidoMaterno','Nombres','Servicio','Telefono','Email','Direccion','CodigoPostal']