# Generated by Django 5.1.4 on 2025-01-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_coluna_quadro_tarefa_coluna_coluna_quadro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='coluna',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='quadro',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='tipo',
            field=models.CharField(blank=True, choices=[('0', 'Para fazer'), ('1', 'Em progresso'), ('2', 'Concluída')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Coluna',
        ),
        migrations.DeleteModel(
            name='Quadro',
        ),
    ]