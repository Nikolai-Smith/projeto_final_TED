from django.shortcuts import redirect, render
from .models import Aluno
from .forms import AlunoForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def listar_alunos(request):
  alunos = Aluno.objects.all()
  return render(request, 'alunos/listar_alunos.html', {'alunos' : alunos})

@login_required()
def cadastrar_alunos(request):
  if request.method == 'POST':
    form = AlunoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_alunos')
  else:
    form = AlunoForm()
  return render(request, 'alunos/form_aluno.html', {'form': form})

def listar_aluno_id(request, id):
  aluno = Aluno.objects.get(id=id)
  return render(request, 'alunos/lista_aluno.html', {'aluno': aluno})

@login_required()
def editar_aluno(request, id):
  aluno = Aluno.objects.get(id=id)
  form = AlunoForm(request.POST or None, instance=aluno)
  if form.is_valid():
    form.save()
    return redirect('listar_alunos')
  return render(request, 'alunos/form_aluno.html', {'form': form})

@login_required()
def remover_aluno(request, id):
  aluno = Aluno.objects.get(id=id)
  if request.method == 'POST':
    aluno.delete()
    return redirect('listar_alunos')
  return render(request, 'alunos/confirma_exclusao.html', {'aluno': aluno}) 

def cadastrar_professor(request):
  if request.method == 'POST':
    form_professor = UserCreationForm(request.POST)
    if form_professor.is_valid():
      form_professor.save()
      return redirect('listar_alunos')
  else:
    form_professor = UserCreationForm()
  return render(request, 'alunos/form_professor.html', {'form_professor': form_professor})

def logar_professor(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    professor = authenticate(request, username=username, password=password)
    if professor is not None:
      login(request, professor)
      return redirect('listar_alunos')
    else:
      messages.error(request, 'login inválido,verifique suas credenciais e tente novamente')
      return redirect('logar_professor')
  else:
    form_login = AuthenticationForm()
  return render(request, 'alunos/form_login.html', {'form_login': form_login})


def deslogar_professor(request):
  logout(request)
  return redirect('logar_professor')
