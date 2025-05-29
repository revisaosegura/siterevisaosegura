from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import cloudinary.uploader
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        celular = request.POST.get('Celular')
        mensagem = request.POST.get('mensagem')

        assunto = 'Nova Mensagem de Contato pelo Site'
        corpo = f"""
Mensagem recebida pelo formulário de contato:

Nome: {nome}
E-mail: {email}
Celular: {celular}
Mensagem: {mensagem}
""".strip()

        send_mail(
            assunto,
            corpo,
            'no-reply@revisaosegura.com.br',
            ['contato@revisaosegura.com.br'],
            fail_silently=False,
        )

        messages.success(request, 'Mensagem enviada com sucesso! Em breve responderemos.')
        return redirect('/contato/')

    return render(request, 'contato.html')

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

        # ✅ Envia por e-mail
        assunto = 'Nova Solicitação de Cálculo Revisional'
        corpo = f"""
Nova ficha de cálculo enviada pelo site:

Nome: {nome}
WhatsApp: {whatsapp}
E-mail: {email}
Valor do Contrato: {valor_total}
Total de Parcelas: {qtd_parcelas}
Parcelas Pagas: {parcelas_pagas}
Valor das Parcelas: {valor_parcela}
Mensagem: {mensagem or '---'}
""".strip()

        send_mail(
            assunto,
            corpo,
            'no-reply@revisaosegura.com.br',
            ['cadastro@revisaosegura.com.br'],
            fail_silently=False,
        )

        messages.success(request, 'Solicitação enviada com sucesso! Entraremos em contato pelo WhatsApp em breve.')
        return redirect('/calculo/')

    return render(request, 'calculo.html')

def servicos(request):
    return render(request, 'servicos.html')

def upload_documento(request):
    if request.method == 'POST' and request.FILES.get('file'):
        arquivo = request.FILES['file']
        resultado = cloudinary.uploader.upload(arquivo)
        return JsonResponse({'url': resultado['secure_url']})

    return JsonResponse({'error': 'Nenhum arquivo enviado'}, status=400)
