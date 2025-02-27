from rest_framework import serializers
from revisao_segura.boletos.models import Boleto

class BoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        fields = ["id", "usuario", "valor", "data_vencimento", "status"]
