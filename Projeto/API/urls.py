from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TarefaViewSet

router = SimpleRouter()
router.register('tarefa', TarefaViewSet)

#Rotas locais
#urlpatterns = [
#    path('tarefa/')
#]