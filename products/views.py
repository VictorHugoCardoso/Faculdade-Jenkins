from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .models import Product
from .forms import ProductForm, NotasForm , AlunoForm,  AlunoDisciplinaForm, DisciplinaForm

from .models import Disciplina
from .models import Aluno
from .models import AlunoDisciplina
from .models import Frequencia
from .models import Notas
from datetime import date


def list_disciplinas(request):
    disciplinas = Disciplina.objects.all()

    today = date.today()
    current_date = today.strftime("%Y-%m-%d")

    return render(request, 'disciplina.html', {'disciplinas': disciplinas, 'current_date': current_date})


def prepararChamada(disciplina_id, data):
    alunos = AlunoDisciplina.objects.filter(discliplina_id=disciplina_id)
    for aluno in alunos:
        freq = Frequencia()

        freq.aluno = aluno.aluno
        freq.discliplina_id = disciplina_id
        freq.presente = 0
        freq.data = data
        freq.save(freq)

    return Frequencia.objects.filter(discliplina_id=disciplina_id, data=data)


def list_frequencias(request, id, date):
    alunos = Frequencia.objects.filter(discliplina_id=id, data=date)
    disciplina_nome = Disciplina.objects.filter(id=id);

    if (alunos.count() == 0):
        alunos = prepararChamada(id, date)

    return render(request, 'frequencias.html',
                  {'alunos': alunos, 'dataFreq': date, 'disciplina_id': id, 'disciplina_nome': disciplina_nome[0]})


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})


def change_status(request, disciplina_id, aluno_id, data):
    freq = Frequencia.objects.filter(discliplina_id=disciplina_id, aluno_id=aluno_id, data=data)[0]
    newFreq = freq

    if freq.presente == 0 or freq.presente == 2:
        newFreq.presente = 1
    elif freq.presente == 1:
        newFreq.presente = 2

    freq = Frequencia.objects.get(id=freq.id)
    freq.delete()
    newFreq.save()

    alunos = Frequencia.objects.filter(discliplina_id=disciplina_id, data=data)
    disciplina_nome = Disciplina.objects.filter(id=disciplina_id);

    if (alunos.count() == 0):
        alunos = prepararChamada(disciplina_id, date)

    return render(request, 'frequencias.html', {'alunos': alunos, 'dataFreq': data, 'disciplina_id': disciplina_id,
                                                'disciplina_nome': disciplina_nome[0]})
def create_notas(request):
    form = NotasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_alunos')

    return render(request, 'notas-form.html', {'form': form})

def create_aluno(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_alunos')

    return render(request, 'aluno-form.html', {'form': form})

def create_aluno_disciplina(request):

    form = AlunoDisciplinaForm(request.POST)

    if form.is_valid() :
        form.save()

        return redirect('create_notas')
    return render(request, 'AlunoDisciplina-form.html', {'form': form})





def update_disciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('list_disciplinas')

    return render(request, 'disciplina-form.html', {'form': form, 'disciplinas': disciplina})

def update_notas(request, id):
    notas = Notas.objects.get(aluno=id)
    form = NotasForm(request.POST or None, instance=notas)

    if form.is_valid():
        form.save()
        return redirect('list_disciplinas')

    return render(request, 'notas-form.html', {'form': form, 'notas': notas})

def update_aluno(request, id):
    aluno= Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('list_alunos')

    return render(request, 'aluno-form.html', {'form': form, 'aluno': aluno})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})

def delete_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('list_alunos')

    return render(request, 'aluno-delete-confirm.html', {'aluno': aluno})


def list_notas(request, id):
    notas_alunos = Notas.objects.filter(discliplina_id=id)
    return render(request, 'notas.html', {'notas_alunos': notas_alunos})


def list_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})

def create_disciplina(request):
    form = DisciplinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_disciplinas')

    return render(request, 'disciplina-form.html', {'form': form})