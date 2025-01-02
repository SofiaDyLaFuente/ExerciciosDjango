from django.db import models

class Base(models.Model):

    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Tarefa(Base):

    escolhas = (
        ("A", "Alta"), 
        ("M", "Média"),
        ("B", "Baixa")
    )
    
    titulo = models.CharField(max_length = 500, null = False, blank = False)
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_conclusao = models.DateField(null = True, blank = True)
    descricao = models.TextField(max_length=1000, blank = True)
    prioridade = models.CharField(max_length=1, choices= escolhas, blank = True)
    #tipo = 

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['id']

    
    def __str__(self):
        return self.titulo