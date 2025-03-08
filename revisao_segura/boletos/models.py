from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField

class Boleto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Correção aqui
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=[('pago', 'Pago'), ('pendente', 'Pendente'), ('vencido', 'Vencido')]
    )
    arquivo = models.FileField(upload_to="boletos/", null=True, blank=True)
    arquivo = CloudinaryField('documentos/')

    def __str__(self):
        return f"Boleto de R$ {self.valor} - Vencimento: {self.vencimento}"

def processar_boletos():
    from boletos.models import Boleto  # Importação dentro da função
    boletos = Boleto.objects.all()
    for boleto in boletos:
        print(boleto)
