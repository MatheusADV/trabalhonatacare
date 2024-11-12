from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class especialidades(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

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
        return f"{self.logradouro}, {self.numero}, {self.complemento + ','  if self.complemento  else ''} {self.bairro} - {self.cep}, {self.cidade}/{self.estado}"

class clinica(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10, unique=True)
    endereco = models.OneToOneField(endereco, on_delete=models.CASCADE)
    plano = models.ManyToManyField(plano, blank=True)
    especialidades = models.ManyToManyField(especialidades, blank=True)
    foto = models.ImageField(blank=True, upload_to='imagens_clin/')
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
class usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length=11)
    endereco = models.OneToOneField(endereco, on_delete=models.CASCADE)
    fav_clin = models.ManyToManyField(clinica, blank=True, related_name="clin_fav")

    def __str__(self):
        return self.nome

class historico(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['data']
        unique_together = ['usuario', 'clinica']

    def __str__(self):
        return self.usuario.nome and self.clinica.nome

class comentario(models.Model):
    comentario = models.TextField()
    avaliacao = models.BooleanField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)




