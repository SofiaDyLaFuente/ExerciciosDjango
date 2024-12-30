from django.db import models

class Base(models.Model):

    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Tarefa(Base):

    escolhas = (
        ("A", "alta"), 
        ("M", "média"),
        ("B", "baixa")
    )
    
    titulo = models.CharField(max_length = 500, null = False, blank = False)
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_conclusao = models.DateTimeField()
    descricao = models.TextField(max_length=1000)
    prioridade = models.CharField(max_length=1, choices= escolhas)
    #tipo = 

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['id']

    
    def __str__(self):
        return self.titulo