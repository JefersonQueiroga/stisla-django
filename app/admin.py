from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Aluno,MiniCurso,Curso
# Register your models here.
admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(MiniCurso)
