from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'sintomas']
        widgets = {
            'nome':forms.TextInput(attrs={'class':"form-control",'id':'nome', 'required': True}),
            'cpf':forms.TextInput(attrs={'class':"form-control",'id':'cpf', 'required': True}),
            'email':forms.EmailInput(attrs={'class':"form-control",'id':'email', 'required': True}),
            'telefone':forms.TextInput(attrs={'class':"form-control",'id':'telefone', 'required': True}),
            'data_nascimento':forms.DateInput(attrs={'class':"form-control",'id':'data_nascimento', 'type': 'date', 'required': True}),
            'sintomas':forms.Textarea(attrs={'class':"form-control",'id':'sintomas', 'required': True}),
        }
        error_messages = {
            'nome': {
                'required': 'O nome é obrigatório.'
            },
            'cpf': {
                'required': 'O CPF é obrigatório.'
            },
            'email': {
                'required': 'O email é obrigatório.'
            },
            'telefone': {
                'required': 'O telefone é obrigatório.'
            },
            'data_nascimento': {
                'required': 'A data de nascimento é obrigatória.'
            },
            'sintomas': {
                'required': 'Os sintomas são obrigatórios.'
            }
        }