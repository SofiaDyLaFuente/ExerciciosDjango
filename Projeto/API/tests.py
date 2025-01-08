from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tarefa


# Teste de rota
class TestRota(APITestCase):
    def testRotaTarefa(self):
        response = self.client.get('/api/v1/tarefa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Teste para criar um novo usuário e criar uma nova tarefa
class TestPost(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")
        self.url = '/api/v1/tarefa/'

    def testCreate(self):
        novaTarefa = {
            "tipo": '0',
            "titulo": 'Tarefa de teste',
            "data_criacao": '2025-01-08',
            "data_conclusao": '2025-01-09',
            "descricao": 'Descrição de teste',
            "prioridade": 'M',
        }
        response = self.client.post(self.url, data=novaTarefa)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], novaTarefa['titulo'])


# Teste para criar uma nova tarefa e depois atualizá-la
class TestPut(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")
        self.tarefa = Tarefa.objects.create(
            tipo='0',
            titulo='Tarefa antiga',
            data_criacao='2025-01-08',
            data_conclusao='2025-01-10',
            descricao='Descrição antiga',
            prioridade='M',
        )
        self.url = f'/api/v1/tarefa/{self.tarefa.id}/'

    def testUpdate(self):
        tarefaAtualizada = {
            "tipo": '1',
            "titulo": 'Tarefa atualizada',
            "data_criacao": '2025-01-08',
            "data_conclusao": '2025-01-10',
            "descricao": 'Descrição atualizada',
            "prioridade": 'A',
        }
        response = self.client.put(self.url, data=tarefaAtualizada)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], tarefaAtualizada['titulo'])


# Teste que cria um novo usuário, cria uma nova tarefa e depois a exclui
class TestDelete(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")
        self.tarefa = Tarefa.objects.create(
            tipo='0',
            titulo='Tarefa para excluir',
            data_criacao='2025-01-08',
            data_conclusao='2025-01-09',
            descricao='Descrição para excluir',
            prioridade='B',
        )
        self.url = f'/api/v1/tarefa/{self.tarefa.id}/'

    def testDelete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tarefa.objects.filter(id=self.tarefa.id).exists())


# Teste para verificar se usuários sem autenticação podem visualizar as tarefas
class TestPermissoes(APITestCase):
    def testAnonimo(self):
        response = self.client.get('/api/v1/tarefa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Esse teste deve falhar, porque usuários sem autenticação não podem criar tarefas. Retornando o erro 403
    def testCriarTarefaAnonimo(self):
        novaTarefa = {
            "tipo": '0',
            "titulo": 'Tarefa sem login',
            "data_criacao": '2025-01-08',
            "data_conclusao": '2025-01-09',
            "descricao": 'Sem login',
            "prioridade": 'B',
        }
        response = self.client.post('/api/v1/tarefa/', data=novaTarefa)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)