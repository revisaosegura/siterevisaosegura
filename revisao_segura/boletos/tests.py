from django.test import TestCase
from django.contrib.auth import get_user_model
from revisao_segura.boletos.models import Boleto

User = get_user_model()

class BoletoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="123456")
        self.boleto = Boleto.objects.create(
            usuario=self.user, valor=100.00, data_vencimento="2025-12-31", status="pendente"
        )

    def test_boleto_creation(self):
        self.assertEqual(self.boleto.usuario.username, "testuser")
        self.assertEqual(self.boleto.valor, 100.00)
        self.assertEqual(self.boleto.status, "pendente")
