from django import forms
from app.models import Aluno,Curso

class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields= '__all__'   

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
    
    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['curso'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['endereco'].widget.attrs['class'] = 'form-control'