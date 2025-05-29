from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from revisao_segura.usuarios.forms import UserRegisterForm  
from revisao_segura.usuarios.models import Usuario, Documento
from .forms import PerfilForm, DocumentoClienteForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
import cloudinary.uploader
from .models import CalculoRevisional

def cadastro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))  # 🔹 Corrigido
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('dashboard'))  # 🔹 Corrigido
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def dashboard(request):
    form_cliente = DocumentoClienteForm()
    
    documentos_cliente = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=True)
    documentos_admin = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=False)

    print(f"Usuário: {request.user}")  
    print(f"Documentos encontrados: {documentos_cliente}, {documentos_admin}")  

    return render(request, "usuarios/dashboard.html", {
        "form_cliente": form_cliente,
        "documentos_cliente": documentos_cliente,
        "documentos_admin": documentos_admin,
    })
      
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
            user = form.save(commit=False)

            if senha_atual and nova_senha and confirmar_senha:
                if not request.user.check_password(senha_atual):
                    messages.error(request, 'Senha atual incorreta.')
                elif nova_senha != confirmar_senha:
                    messages.error(request, 'A nova senha e a confirmação não coincidem.')
                else:
                    user.set_password(nova_senha)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Senha alterada com sucesso!')
                    return redirect(reverse('perfil'))

            messages.success(request, 'Perfil atualizado com sucesso!')
            user.save()
            return redirect(reverse('editar_perfil'))  # 🔹 Corrigido
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def upload_documento(request):
    if request.method == "POST":
        form = DocumentoClienteForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.usuario = request.user
            documento.save()
            messages.success(request, "Documento enviado com sucesso!")
        else:
            messages.error(request, "Erro ao enviar documento.")
        return redirect(reverse('dashboard'))  # 🔹 Corrigido

    form = DocumentoClienteForm()
    documentos = Documento.objects.filter(usuario=request.user)
    return render(request, "usuarios/dashboard.html", {"form": form, "documentos": documentos})

@login_required
def enviar_documento_cliente(request):
    if request.method == "POST":
        form = DocumentoClienteForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.usuario = request.user
            documento.enviado_pelo_cliente = True  
            documento.status = "pendente"

            # 🔹 Upload para Cloudinary (aceitando PDFs corretamente)
            resultado = cloudinary.uploader.upload(
                request.FILES['arquivo'],
                resource_type="raw"  # 🔹 Define como "raw" para aceitar PDFs
            )
            
            documento.url_arquivo = resultado['secure_url'].replace("/image/", "/raw/")
            documento.save()
            messages.success(request, "Documento enviado com sucesso!")
        else:
            messages.error(request, "Erro ao enviar o documento. Verifique o arquivo.")
        return redirect(reverse('dashboard'))  # 🔹 Corrigido

    form_cliente = DocumentoClienteForm()
    documentos_cliente = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=True)
    documentos_admin = Documento.objects.filter(usuario=request.user, enviado_pelo_cliente=False)

    return render(request, "usuarios/dashboard.html", {
        "form_cliente": form_cliente,
        "documentos_cliente": documentos_cliente,
        "documentos_admin": documentos_admin
    })

@login_required
def excluir_documento(request, documento_id):
    documento = get_object_or_404(Documento, id=documento_id)

    if documento.usuario == request.user:
        documento.delete()
        messages.success(request, "Documento excluído com sucesso.")
    else:
        messages.error(request, "Você não tem permissão para excluir este documento.")

    return redirect(reverse('dashboard'))  # 🔹 Corrigido

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))  # 🔹 Corrigido

def enviar_para_telegram(token, chat_ids, mensagem):
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": mensagem,
            "parse_mode": "Markdown"
        }
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Erro ao enviar para o Telegram: {e}")

def calculo_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        whatsapp = request.POST.get('whatsapp')
        email = request.POST.get('email')
        valor_total = request.POST.get('valor_total')
        qtd_parcelas = request.POST.get('qtd_parcelas')
        parcelas_pagas = request.POST.get('parcelas_pagas')
        valor_parcela = request.POST.get('valor_parcela')
        mensagem = request.POST.get('mensagem')

        # ✅ Salva no admin
        CalculoRevisional.objects.create(
            nome=nome,
            whatsapp=whatsapp,
            email=email,
            valor_total=valor_total,
            qtd_parcelas=qtd_parcelas,
            parcelas_pagas=parcelas_pagas,
            valor_parcela=valor_parcela,
            mensagem=mensagem
        )

        # ✅ Envia a ficha para o Telegram
        token = "SEU_TOKEN_DO_BOT"
        chat_ids = ["SEU_CHAT_ID"]  # pode ser uma lista com 1 ou mais IDs
        texto = f"""
*Nova Solicitação de Cálculo Revisional*
📌 *Nome:* {nome}
📞 *WhatsApp:* {whatsapp}
📧 *E-mail:* {email}
💰 *Valor do Contrato:* {valor_total}
📆 *Total de Parcelas:* {qtd_parcelas}
✅ *Parcelas Pagas:* {parcelas_pagas}
💳 *Valor das Parcelas:* {valor_parcela}
📝 *Mensagem:* {mensagem or '---'}
""".strip()

        enviar_para_telegram(token, chat_ids, texto)

        messages.success(request, 'Solicitação enviada com sucesso! Entraremos em contato pelo WhatsApp em breve.')
        return redirect('/calculo/')

    return render(request, 'calculo.html')
