from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['first_name', 'last_name', 'email', 'sexo', 'birth_date']