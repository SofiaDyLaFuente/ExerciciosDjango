from django.shortcuts import render
from .models import Tarefa
from rest_framework.response import Response
from .serializer import TarefaSerializer
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

class TarefaViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo']

    def OrganizarPorTipo(self, request, *args, **kwargs):
        # Agrupar tarefas por tipo
        tarefas = Tarefa.objects.all()

        # Filtrar as tarefas por tipo
        tarefasOrganizadas = {
            'para_fazer': tarefas.filter(tipo='0'),  
            'em_progresso': tarefas.filter(tipo='1'),  
            'concluida': tarefas.filter(tipo='2'),  
        }

        # Serializar cada grupo de tarefa
        serializer0 = TarefaSerializer(tarefasOrganizadas['para_fazer'], many=True)
        serializer1 = TarefaSerializer(tarefasOrganizadas['em_progresso'], many=True)
        serializer2 = TarefaSerializer(tarefasOrganizadas['concluida'], many=True)

        # Retornar as tarefas agrupadas no formato JSON
        return Response({
            'para_fazer': serializer0.data,
            'em_progresso': serializer1.data,
            'concluida': serializer2.data
        })