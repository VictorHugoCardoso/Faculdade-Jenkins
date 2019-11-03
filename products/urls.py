from django.urls import path
from .views import list_products, list_alunos, create_product, create_aluno_disciplina, create_notas,  create_aluno, create_disciplina, update_disciplina, update_product, update_aluno, update_notas, delete_product, delete_aluno, list_disciplinas,list_frequencias,list_notas, change_status

urlpatterns = [
    path('example/', list_products, name='list_products'),
    path('example/new', create_product, name='create_products'),
    path('example/update/<int:id>/', update_product, name='update_product'),
    path('example/delete/<int:id>/', delete_product, name='delete_product'),
    path('notas/new_notas', create_notas, name='create_notas'),
    path('notas/<int:id>', list_notas, name='list_notas'),
    path('notas/update/<int:id>', update_notas, name='update_notas'),
    path('notas/new_notas', create_notas, name='create_notas'),
    path('disciplina/new_disciplina', create_disciplina, name='create_disciplina'),
    path('disciplina/update/<int:id>', update_disciplina, name='update_disciplina'),
    path('disciplinas/', list_disciplinas, name='list_disciplinas'),
    path('frequencias/<int:id>/<str:date>', list_frequencias, name='list_frequencias'),
   path('alunos/', list_alunos, name='list_alunos'),
    path('aluno/update/<int:id>', update_aluno, name='update_aluno'),
    path('aluno/delete/<int:id>/', delete_aluno, name='delete_aluno'),
    path('aluno/new/', create_aluno, name='create_aluno'),
    path('aluno/new-aluno-disciplina/', create_aluno_disciplina, name='create_aluno_disciplina'),
    path('change_status/<int:disciplina_id>/<int:aluno_id>/<str:data>', change_status, name='change_status')

]


# CRUD - CREATE, READ, UPDATE, DELETE