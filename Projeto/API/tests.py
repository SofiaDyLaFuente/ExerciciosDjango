from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tarefa
from rest_framework import status
import requests
from rest_framework.test import APITestCase



# Test de rota
class TesteRota(APITestCase):

    def test_rota_tarefas(self):
        response = self.client.get('http://localhost:8000/api/v1/tarefa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
class TestPost(APITestCase):

    """
    def test_nova_tarefa(self):

       novo = {
            "tipo" = '0',
            "titulo" = 'Tarefa de teste 6',
            "data_criacao" = '2025-01-08',
            "data_conclusao" = '2025-01-08',
            "descriçao" = 'Tarefa de teste',
            "prioridade" = 'M',
        }
            

        resposta = requests.post(url='http://localhost:8000/api/v1/tarefa/', data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['tipo'] == novo['tipo']


"""