from django.shortcuts import render
from .models import Tarefa
from rest_framework.response import Response
from .serializer import TarefaSerializer
from rest_framework import viewsets, mixins

class TarefaViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    