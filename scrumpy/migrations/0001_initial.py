# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('url', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('proyecto', models.ForeignKey(to='scrumpy.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('estado', models.CharField(default='Pendiente', max_length=12, choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('En pruebas', 'En pruebas'), ('Completado', 'Completado')])),
                ('seccion', models.ForeignKey(to='scrumpy.Seccion')),
            ],
        ),
    ]
