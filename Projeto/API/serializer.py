from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = (
            'tipo',
            'titulo',
            'data_criacao',
            'data_conclusao',
            'descricao',
            'prioridade',   
        )
        extra_kwargs = {
            'email': {'write_only': True}

        }
