from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TarefaViewSet, QuadroViewSet, ListaViewSet

router = SimpleRouter()
router.register('tarefa', TarefaViewSet)
router.register('lista', ListaViewSet)
router.register('quadro', QuadroViewSet)

