# Generated by Django 5.1.4 on 2025-01-06 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_tarefa_lista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='quadro',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='lista',
        ),
        migrations.DeleteModel(
            name='Quadro',
        ),
        migrations.DeleteModel(
            name='Lista',
        ),
    ]
