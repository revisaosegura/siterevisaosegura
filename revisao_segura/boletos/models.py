from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.models

class Boleto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 🔹 Correção aqui
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()  # 🔹 Corrigido para ser um campo de data válido
    status = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("pago", "Pago")])
    documento = cloudinary.models.CloudinaryField('documento', null=True, blank=True)  # 🔹 Armazena o documento no Cloudinary
    arquivo = models.URLField()  # URL do arquivo armazenado no Cloudinary

    def __str__(self):
        return f"Boleto de R$ {self.valor} - Vencimento: {self.vencimento}"

def processar_boletos():
    from boletos.models import Boleto  # Importação dentro da função
    boletos = Boleto.objects.all()
    for boleto in boletos:
        print(boleto)
