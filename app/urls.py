from django.urls import path
from app.views import cadastro_aluno,index,update_aluno,remover_aluno
urlpatterns = [
    path('cadastro_aluno',cadastro_aluno, name='cadastro_aluno'),
    path('editar/<int:pk>/', update_aluno, name='editar_aluno'),
    path('remover/<int:pk>/', remover_aluno, name='remover_aluno'),
    path('',index,name="index"),
]
