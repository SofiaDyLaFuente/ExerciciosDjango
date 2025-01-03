from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'titulo', 'data_criacao', 'data_conclusao', 'descricao', 'prioridade')
