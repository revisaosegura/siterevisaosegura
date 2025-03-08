from django.contrib import admin
from revisao_segura.boletos.models import Boleto 

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'valor', 'data_vencimento', 'status', 'arquivo')  # ✅ Corrigido
    list_filter = ('status', 'data_vencimento')
    search_fields = ('usuario__username', 'valor', 'status')
    fields = ('usuario', 'valor', 'data_vencimento', 'status', 'arquivo')  # ✅ Usando os campos certos
