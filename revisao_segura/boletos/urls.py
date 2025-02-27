from django.urls import path
from . import views  # Certifique-se de importar o módulo views corretamente

urlpatterns = [
    path('', views.listar_boletos, name='listar_boletos'),  # Corrigido para "listar_boletos"
    path('<int:boleto_id>/', views.detalhar_boleto, name='detalhar_boleto'),
    path('gerar_boleto/<int:boleto_id>/', views.gerar_boleto, name='gerar_boleto'),
]

