# Generated by Django 2.0.2 on 2018-08-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skywalker', '0005_auto_20180809_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='quantidade_alunos',
        ),
    ]
