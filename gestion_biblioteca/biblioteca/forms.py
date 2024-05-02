from django import forms # type: ignore
from .models import Usuario, Libro, Prestamo

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }

class BusquedaLibroForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), label='Seleccionar libro', required=False)
