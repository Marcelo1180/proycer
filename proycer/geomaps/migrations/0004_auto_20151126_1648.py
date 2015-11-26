# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('geomaps', '0003_auto_20151120_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('canton', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distrito', models.CharField(max_length=150)),
                ('canton', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'canton', to='geomaps.Canton', chained_field=b'canton')),
                ('departamento', models.ForeignKey(to='geomaps.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localidad', models.CharField(max_length=150)),
                ('canton', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'canton', to='geomaps.Canton', chained_field=b'canton')),
                ('departamento', models.ForeignKey(to='geomaps.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provincia', models.CharField(max_length=150)),
                ('departamento', models.ForeignKey(to='geomaps.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seccion', models.CharField(max_length=150)),
                ('departamento', models.ForeignKey(to='geomaps.Departamento')),
                ('provincia', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', to='geomaps.Provincia', chained_field=b'departamento')),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', to='geomaps.Provincia', chained_field=b'departamento'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='seccion',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'provincia', to='geomaps.Seccion', chained_field=b'provincia'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='localidad',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'localidad', to='geomaps.Localidad', chained_field=b'localidad'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', to='geomaps.Provincia', chained_field=b'departamento'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='seccion',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'provincia', to='geomaps.Seccion', chained_field=b'provincia'),
        ),
        migrations.AddField(
            model_name='canton',
            name='departamento',
            field=models.ForeignKey(to='geomaps.Departamento'),
        ),
        migrations.AddField(
            model_name='canton',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', to='geomaps.Provincia', chained_field=b'departamento'),
        ),
        migrations.AddField(
            model_name='canton',
            name='seccion',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'provincia', to='geomaps.Seccion', chained_field=b'provincia'),
        ),
    ]
