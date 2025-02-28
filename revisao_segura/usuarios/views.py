from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from revisao_segura.usuarios.forms import UserRegisterForm  # 🔹 Correção da importação
from revisao_segura.usuarios.models import Usuario  # 🔹 Correção da importação
from revisao_segura.usuarios.models import Documento
from .forms import PerfilForm
from .forms import DocumentoClienteForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def dashboard(request):
    form_cliente = DocumentoClienteForm()
    
    # Pega todos os documentos que o usuário enviou
    documentos_cliente = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=True)

    # Pega todos os documentos que o ADMIN enviou para esse usuário
    documentos_admin = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=False)

    return render(request, "dashboard.html", {
        "form_cliente": form_cliente,
        "documentos_cliente": documentos_cliente,
        "documentos_admin": documentos_admin,
    })
      
    print(f"Usuário: {request.user}")  # Depuração
    print(f"Documentos encontrados: {documentos}")  # Depuração
    
    return render(request, "dashboard.html", {"documentos": documentos})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        senha_atual = request.POST.get('senha_atual')
        nova_senha = request.POST.get('nova_senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if form.is_valid():
            form.save()
            return redirect('perfil')
            if senha_atual and nova_senha and confirmar_senha:
                if not request.user.check_password(senha_atual):
                    messages.error(request, 'Senha atual incorreta.')
                elif nova_senha != confirmar_senha:
                    messages.error(request, 'A nova senha e a confirmação não coincidem.')
                else:
                    user.set_password(nova_senha)
                    user.save()
                    update_session_auth_hash(request, user)  # Mantém o usuário logado após a troca de senha
                    messages.success(request, 'Senha alterada com sucesso!')

            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuarios/editar_perfil')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def upload_documento(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.usuario = request.user
            documento.save()
            messages.success(request, "Documento enviado com sucesso!")
        else:
            messages.error(request, "Erro ao enviar documento.")
        return redirect("dashboard")

    form = DocumentoForm()
    documentos = Documento.objects.filter(usuario=request.user)
    return render(request, "dashboard.html", {"form": form, "documentos": documentos})

@login_required
def enviar_documento_cliente(request):
    if request.method == "POST":
        form = DocumentoClienteForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.usuario = request.user
            documento.enviado_pelo_cliente = True  # Define que foi enviado pelo cliente
            documento.status = "pendente"  # O admin precisará aprovar
            documento.save()

            messages.success(request, "Documento enviado com sucesso!")  # Adiciona a mensagem
            return redirect('dashboard')  # Redireciona para evitar reenvio do formulário
        else:
            messages.error(request, "Erro ao enviar o documento. Verifique o arquivo.")
            return redirect('dashboard')  # Retorna ao dashboard se houver erro

    form = DocumentoClienteForm()
    documentos_cliente = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=True)
    documentos_admin = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=False)

    return render(request, "dashboard.html", {
        "form_cliente": form_cliente,
        "documentos_cliente": documentos_cliente,
        "documentos_admin": documentos_admin
    })

@login_required
def excluir_documento(request, documento_id):
    documento = get_object_or_404(Documento, id=documento_id)

    # Verifica se o documento pertence ao usuário
    if documento.usuario == request.user:
        documento.delete()
        messages.success(request, "Documento excluído com sucesso.")
    else:
        messages.error(request, "Você não tem permissão para excluir este documento.")

    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')

def delete_all_users(request):
    User.objects.all().delete()
    return HttpResponse("Todos os usuários foram excluídos com sucesso!")

