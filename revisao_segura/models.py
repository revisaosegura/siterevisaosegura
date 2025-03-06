from django.db import models
from cloudinary.models import CloudinaryField

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = CloudinaryField('documentos/')  # Armazena no Cloudinary automaticamente
