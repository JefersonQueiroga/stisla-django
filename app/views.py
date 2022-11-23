from django.shortcuts import render
from app.forms import AlunoForm
from django.shortcuts import redirect,get_object_or_404
from app.models import Aluno
from django.core.paginator import Paginator

def index(request):
    alunos_list = Aluno.objects.all()
    
    paginator = Paginator(alunos_list, 5)

    page = request.GET.get('page')

    alunos = paginator.get_page(page)

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



def update_aluno(request, pk):
    book= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, "cadastro_aluno.html", {'form':form})