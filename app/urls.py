from django.urls import path
from app.views import cadastro_aluno,index,update_aluno

urlpatterns = [
    path('cadastro_aluno',cadastro_aluno, name='cadastro_aluno'),
    path('editar/<int:pk>/', update_aluno, name='editar_aluno'),
    path('',index,name="index"),
]
