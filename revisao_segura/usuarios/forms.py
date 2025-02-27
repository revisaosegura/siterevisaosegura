from django import forms
from django.contrib.auth.forms import UserCreationForm
from revisao_segura.usuarios.models import Usuario  # 🔹 Correção da importação
from .models import Documento

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ["username", "email", "cpf", "telefone", "password1", "password2"]

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario  # Se estiver usando um modelo personalizado, substitua por ele
        fields = ['first_name', 'last_name', 'email']  # Adicione mais campos se necessário

class DocumentoClienteForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['arquivo']
        widgets = {
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
        }
