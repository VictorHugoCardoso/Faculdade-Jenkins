from django import forms
from .models import Product
from  .models import Notas
from .models import  Aluno
from  .models import  AlunoDisciplina
from .models import Disciplina


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'quantity']


class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['id','nota1','nota2','nota3','nota4','aluno','discliplina']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['id','nomeAluno']

class AlunoDisciplinaForm(forms.ModelForm):
    class Meta:
        model = AlunoDisciplina
        fields = ['id','aluno', 'discliplina']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['id','nomeDisciplina']
