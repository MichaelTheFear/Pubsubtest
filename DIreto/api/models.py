from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=8)
    email = models.EmailField(primary_key=True)
    informante = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField('Categoria', related_name='usuarios')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ManyToManyField('Categoria', related_name='posts')

    def __str__(self):
        return self.title
