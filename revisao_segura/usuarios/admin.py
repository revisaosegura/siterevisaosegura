from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from revisao_segura.usuarios.models import Usuario  # 🔹 Correção da importação
from .models import Documento

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
