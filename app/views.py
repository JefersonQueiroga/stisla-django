from django.shortcuts import render
from app.forms import AlunoForm
from django.shortcuts import redirect,get_object_or_404
from app.models import Aluno
from django.views.generic import TemplateView,ListView
from .filters import AlunoFilter
import sweetify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    alunos = Aluno.objects.all()
    return render(request,'index.html',{'alunos':alunos})

def cadastro_aluno(request):
    form = AlunoForm(request.POST or None)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST) 
        
        if form.is_valid():
            form.save()
            form = AlunoForm()
            return redirect('index')
         

    return render(request, 'cadastro_aluno.html',{ 'form' : form})


@login_required
def update_aluno(request, pk):
    aluno= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        sweetify.sweetalert(request,'Aluno alterado com Sucesso!')
        return redirect('index')
    
    return render(request, "cadastro_aluno.html", {'form':form})

@login_required
def remover_aluno(request, pk):
    aluno= get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('index')


def logout_aplicacao(request):
     logout(request)
     return redirect('login')

class AboutView(TemplateView):
    template_name = "quemsomos.html"

class ListAlunoView(ListView):
    template_name = "lista_aluno.html"
    queryset = Aluno.objects.all()

        
def search_aluno(request):
    aluno_list = Aluno.objects.all()
    aluno_filter = AlunoFilter(request.GET, queryset=aluno_list)
    return render(request, 'aluno_list.html', {'filter': aluno_filter})