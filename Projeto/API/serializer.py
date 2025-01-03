from rest_framework import serializers
from .models import Tarefa, Quadro, Lista
from rest_framework.exceptions import ValidationError

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
    
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
            if value:
                # Verificar se a data de criação foi fornecida e realizar a comparação
                data_criacao = self.initial_data.get('data_criacao')  # Pega a data de criação do dado de entrada
                if not data_criacao:
                    raise ValidationError("A data de criação é obrigatória.")
                
                if value < data_criacao:
                    raise ValidationError("A data de conclusão não pode ser anterior à data da criação.")

            return value

class ListaSerializer(serializers.ModelSerializer):

    tarefas = TarefaSerializer(many = True, read_only = True)
    
    class Meta:
        model = Lista
        fields = ('nome','tarefas')


class QuadroSerializer(serializers.ModelSerializer):

    listas = ListaSerializer(many = True, read_only = True)

    class Meta:
        model = Quadro
        fields = ('nome', 'listas')
