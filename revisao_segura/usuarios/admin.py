from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from revisao_segura.usuarios.models import Usuario  # 🔹 Correção da importação
from .models import Documento, CalculoRevisional, SimulacaoEmprestimo

@admin.register(CalculoRevisional)
class CalculoRevisionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'whatsapp', 'email', 'criado_em']
    search_fields = ['nome', 'whatsapp', 'email']

@admin.register(SimulacaoEmprestimo)
class SimulacaoEmprestimoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'whatsapp', 'situacao_profissional', 'valor_total', 'renda_mensal', 'data_envio')
    list_filter = ('situacao_profissional', 'data_envio')
    search_fields = ('nome', 'email', 'whatsapp')
    ordering = ('-data_envio',)
    
class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ("Informações adicionais", {"fields": ("cpf", "telefone")}),
    )

admin.site.register(Usuario, UsuarioAdmin)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "arquivo", "status", "enviado_pelo_cliente")
    list_filter = ("status", "enviado_pelo_cliente")
    search_fields = ("usuario__username", "arquivo")

