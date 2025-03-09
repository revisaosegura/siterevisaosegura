from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Documento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="documentos")
    titulo = models.CharField(max_length=255, blank=True, null=True)  # Adicionando o campo título
    arquivo = CloudinaryField('arquivo', folder='documentos/', resource_type='auto')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    enviado_pelo_cliente = models.BooleanField(default=False)  # Indica se foi enviado pelo cliente
    arquivo = CloudinaryField('documentos/')

def __str__(self):
        tipo = "Cliente" if self.enviado_pelo_cliente else "Admin"
        return f"Documento de {self.usuario.username} ({tipo}) - {self.get_status_display()}"
