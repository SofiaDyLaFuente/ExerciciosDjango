from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TarefaViewSet

router = SimpleRouter()
router.register('tarefa', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]