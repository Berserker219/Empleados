from django import forms


class NewDepartamentoFomrs(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortName = forms.CharField(max_length=20)
    