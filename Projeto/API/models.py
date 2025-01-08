from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
    data_criacao = models.DateField(null = False, blank = False)
    data_conclusao = models.DateField(null = True, blank = True)
    descricao = models.TextField(max_length=1000, blank = True)
    prioridade = models.CharField(max_length=1, choices= escolhas, blank = True)
    tipo = models.CharField(max_length = 1, choices= colunas, blank = True)


    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['id']

#-----

    def clean(self):
        
        if self.data_conclusao and self.data_criacao and self.data_conclusao < self.data_criacao:
            raise ValidationError("A data de conclusão não pode ser anterior à data de criação.")

    def save(self, *args, **kwargs):

        self.full_clean() 
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo
    