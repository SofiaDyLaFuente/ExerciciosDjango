from django.shortcuts import render
from .models import Tarefa, Quadro, Lista
from rest_framework.response import Response
from .serializer import TarefaSerializer, QuadroSerializer, ListaSerializer
from rest_framework import viewsets, mixins

class TarefaViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer


class QuadroViewSet(viewsets.ModelViewSet):
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer




'''
from django.shortcuts import render
from .models import Tarefa
from .serializer import TarefaSerializer
import requests

def TarefaViewSet(requests):
    tarefas = Tarefa.objects.all()  # Obter todas as tarefas
    return render(requests, 'template.html', {'tarefas': tarefas})

'''