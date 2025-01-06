from .models import Tarefa
from rest_framework.response import Response
from .serializer import TarefaSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def lista(self, request, *args, **kwargs):
        # Organizar as tarefas por tipo
        tarefas = Tarefa.objects.all()

        tarefasOrganizadas = {
            'para_fazer': tarefas.filter(tipo='0'),  
            'em_progresso': tarefas.filter(tipo='1'),  
            'concluida': tarefas.filter(tipo='2'),  
        }

        # Serializar cada grupo de tarefas
        serializer0 = TarefaSerializer(tarefasOrganizadas['para_fazer'], many=True)
        serializer1 = TarefaSerializer(tarefasOrganizadas['em_progresso'], many=True)
        serializer2 = TarefaSerializer(tarefasOrganizadas['concluida'], many=True)

        # Retornar as tarefas organizadas no formato JSON
        return Response({
            'para_fazer': serializer0.data,
            'em_progresso': serializer1.data,
            'concluida': serializer2.data
        })