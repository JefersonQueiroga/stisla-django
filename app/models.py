from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome


class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome


class Aluno(models.Model):
    LIST_SEXO=[('Masculino','Masculino'), ('Feminino','Feminino')]
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateTimeField()
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    sexo = models.CharField(max_length=20, choices=LIST_SEXO,default=None)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    minicursos = models.ManyToManyField(MiniCurso, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome