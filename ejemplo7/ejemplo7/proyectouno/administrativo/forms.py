from django.forms import ModelForm
from django import forms

from administrativo.models import Matricula,Modulo, Estudiante

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']



class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),}

class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']
        widgets = {
            'nombre': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona un módulo'
            }),
        }
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_estudiante': forms.Select(attrs={'class': 'form-control'}),
        }