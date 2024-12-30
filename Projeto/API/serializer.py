from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):

    extra_kwargs = {
            'email': {'write_only':True}
        }
    
    model = Tarefa
    
    fields = (
            'titulo',
            'data_criacao',
            'data_conclusao',
            'descricao',
            'prioridade'      
    )
