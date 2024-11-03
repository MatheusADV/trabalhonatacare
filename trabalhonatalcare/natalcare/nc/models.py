from django.db import models

# Create your models here.

class plano(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='planos', blank=True)

    def __str__(self):
        return self.nome

class endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.logradouro

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length=11)
    endereco = models.OneToOneField(endereco, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome

class clinica(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10, unique=True)
    endereco = models.OneToOneField(endereco, on_delete=models.CASCADE)
    plano = models.ManyToManyField(plano, blank=True)

    def __str__(self):
        return self.nome



