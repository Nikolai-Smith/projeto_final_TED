from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_alunos, name='listar_alunos'),
    path('cadastrar', cadastrar_alunos, name='cadastrar_alunos'),
    path('listar/<int:id>',listar_aluno_id, name='listar_aluno_id'),
    path('editar/<int:id>',editar_aluno, name='editar_aluno'),
    path('remover/<int:id>',remover_aluno, name='remover_aluno'),
    path('cadastrar_professor/', cadastrar_professor, name='cadastrar_professor'),
    path('logar_professor/', logar_professor, name='logar_professor'),
    path('deslogar_professor/', deslogar_professor, name='deslogar_professor'),
]