from .models import Aluno
import django_filters

class AlunoFilter(django_filters.FilterSet):
    class Meta:
        model = Aluno
        fields = ['nome', 'curso', 'minicursos', ]