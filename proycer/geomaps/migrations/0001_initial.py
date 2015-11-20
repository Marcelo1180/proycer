# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=70)),
                ('parteno', models.CharField(max_length=70)),
                ('materno', models.CharField(max_length=70)),
                ('ci', models.CharField(max_length=10)),
                ('telefonos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=70)),
                ('paterno', models.CharField(max_length=70)),
                ('materno', models.CharField(max_length=70)),
                ('ci', models.CharField(max_length=10)),
                ('rda', models.CharField(max_length=10)),
                ('formacion', models.TextField()),
                ('especialidad', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidad', models.CharField(max_length=50)),
                ('area', models.ForeignKey(to='geomaps.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('etapa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UEducativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('departamento', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('zona', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('dependencia', models.CharField(max_length=1, choices=[(b'F', b'Fiscal'), (b'P', b'Privada'), (b'C', b'Convenio')])),
                ('area', models.CharField(max_length=1, choices=[(b'R', b'Rural'), (b'U', b'Urbana')])),
                ('nombre', models.CharField(max_length=100)),
                ('telefonos', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('year_fundation', models.IntegerField()),
                ('internet', models.BooleanField(choices=[(True, b'Si'), (False, b'No')])),
                ('imagen', models.ImageField(upload_to=b'uploads/ueducativa')),
                ('video', models.URLField()),
                ('link_institucional', models.URLField()),
                ('cant_estudiantes', models.IntegerField()),
                ('cant_docentes', models.IntegerField()),
                ('cant_administrativos', models.IntegerField()),
                ('contacto', models.OneToOneField(to='geomaps.Contacto')),
                ('director', models.OneToOneField(to='geomaps.Director')),
                ('especialidad', models.ManyToManyField(to='geomaps.Especialidad')),
                ('etapa', models.ManyToManyField(to='geomaps.Etapa')),
            ],
        ),
        migrations.AddField(
            model_name='etapa',
            name='nivel',
            field=models.ForeignKey(to='geomaps.Nivel'),
        ),
    ]
