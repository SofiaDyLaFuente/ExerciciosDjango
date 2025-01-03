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

    colunas = (
        ("0", "Para fazer"),
        ("1", "Em progresso"),
        ("2", "Concluída")
    )
    
    titulo = models.CharField(max_length = 500, null = False, blank = False)
    data_criacao = models.DateTimeField(auto_now_add = True)
    data_conclusao = models.DateField(null = True, blank = True)
    descricao = models.TextField(max_length=1000, blank = True)
    prioridade = models.CharField(max_length=1, choices= escolhas, blank = True)
    tipo = models.CharField(max_length = 1, choices= colunas, blank = True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['id']

    
    def __str__(self):
        return self.titulo
    

class Lista(models.Model):
    nome = models.CharField(max_length=250)
    quadro = models.ForeignKey(Quadro, on_delete = models.CASCADE, related_name= "Lista")

    def __str__(self):
        return self.nome
    

class Quadro(models.Model):
    nome = models.CharField(max_length = 250)

    def __str__(self):
        return self.nome