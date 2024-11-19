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
    foto = models.ImageField(blank=True, null=True, default="/batman-resolve-in-the-rain.jpg", upload_to="media")
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
        return f"{self.usuario.nome} -> {self.clinica.nome}"

class favorito(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['data']
        unique_together = ['usuario', 'clinica']

    def __str__(self):
        return f"{self.usuario.nome} -> {self.clinica.nome}"
    
class comentarios(models.Model):
    comentario = models.TextField()
    avaliacao = models.BooleanField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario

class chat(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nome} -> {self.clinica.nome}"

class mensagens(models.Model):
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(chat, on_delete=models.CASCADE)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data']

    def __str__(self):
        return self.mensagem