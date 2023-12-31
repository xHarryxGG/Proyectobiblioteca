# Generated by Django 4.2.7 on 2023-11-25 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academico',
            fields=[
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('escuela', models.CharField(choices=[('ingenieria', 'Ingeniería'), ('derecho', 'Derecho'), ('ingenieria_y_derecho', 'Ingeniería y derecho')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='administrativo',
            fields=[
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('semestre', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('carrera', models.CharField(max_length=40)),
                ('escuela', models.CharField(choices=[('ingenieria', 'Ingeniería'), ('derecho', 'Derecho'), ('ingenieria_y_derecho', 'Ingeniería y derecho')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('autor', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cota', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=20)),
                ('edicion', models.CharField(max_length=20)),
                ('año', models.CharField(max_length=20)),
                ('cantidad', models.CharField(default='0', max_length=6)),
                ('cantidadPres', models.CharField(default='0', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='prestamo',
            fields=[
                ('codigo', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('autor', models.CharField(default='', max_length=20)),
                ('titulo', models.CharField(default='', max_length=20)),
                ('usuario', models.CharField(choices=[('1', 'Estudiante'), ('2', 'Academico'), ('3', 'Administrativo')], default='Estudiante', max_length=20)),
                ('nombre', models.CharField(default='', max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('cedula', models.CharField(max_length=8)),
                ('semestre', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('escuela', models.CharField(choices=[('ingenieria', 'Ingeniería'), ('derecho', 'Derecho'), ('ingenieria_y_derecho', 'Ingeniería y derecho')], max_length=40)),
                ('bibliotecaria', models.CharField(max_length=40)),
                ('tipoPrestamo', models.CharField(default='', max_length=20)),
                ('tipoUsuario', models.CharField(default='', max_length=20)),
                ('fechaInicial', models.DateTimeField(default=datetime.date.today)),
                ('fechaFinal', models.DateTimeField(default=datetime.date.today)),
                ('observaciones', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
