# Generated by Django 4.0 on 2022-11-22 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=15)),
                ('data_nascimento', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=20)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.curso')),
                ('minicursos', models.ManyToManyField(blank=True, null=True, to='app.MiniCurso')),
            ],
        ),
    ]
