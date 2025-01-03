from rest_framework import serializers
from .models import Tarefa, Quadro, Lista
from rest_framework.exceptions import ValidationError

class TarefaSerializer(serializers.ModelSerializer):

    extra_kwargs = {
            'email': {'write_only':True}
        }
    
    model = Tarefa
    
    fields = (
            'tipo',
            'titulo',
            'data_criacao',
            'data_conclusao',
            'descricao',
            'prioridade',   
    )

    def validate_data_conclusao(self, value):
        if value and value < self.instance.data_criacao.date():
            raise ValidationError("A data de conclusão não pode ser anterior a data da criação")
        
        return value

class ListaSerializer(serializers.ModelSerializer):

    tarefas = TarefaSerializer(many = True, read_only = True)

    model = Lista
    
    fields = (
            'titulo',
            'nome',
            'quadro',
            'tarefas',      
    )


class QuadroSerializer(serializers.ModelSerializer):

    listas = ListaSerializer(many = True, read_only = True)

    model = Quadro

    fields = (
            'nome',
            'listas',
    )

