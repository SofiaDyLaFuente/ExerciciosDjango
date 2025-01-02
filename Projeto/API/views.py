from django.shortcuts import render
from .models import Tarefa
from rest_framework.response import Response
from .serializer import TarefaSerializer
from rest_framework import viewsets, mixins

class TarefaViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer



'''
from django.shortcuts import render
from .models import Tarefa
from .serializer import TarefaSerializer
import requests

def TarefaViewSet(requests):
    tarefas = Tarefa.objects.all()  # Obter todas as tarefas
    return render(requests, 'template.html', {'tarefas': tarefas})

'''