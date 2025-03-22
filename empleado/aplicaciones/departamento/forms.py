from django import forms


class NewDepartamentoFomrs(forms.Form):
    departamento = forms.CharField(max_length=50)
    shortName = forms.CharField(max_length=20)
    