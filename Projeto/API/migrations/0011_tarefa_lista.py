# Generated by Django 5.1.4 on 2025-01-06 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_alter_tarefa_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='lista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='API.lista'),
            preserve_default=False,
        ),
    ]