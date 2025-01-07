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

#---------

    def create(self, validated_data):
        tarefa = Tarefa(**validated_data)
        tarefa.full_clean()  # Chama a validação global antes de salvar
        tarefa.save()
        return tarefa

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.full_clean()  # Chama a validação global antes de atualizar
        instance.save()
        return instance

