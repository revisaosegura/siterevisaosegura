from rest_framework import viewsets
from boletos.models import Boleto
from revisao_segura.boletos.serializers import BoletoSerializer

class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer

    def get_queryset(self):
        user = self.request.user
        return Boleto.objects.filter(usuario=user)
