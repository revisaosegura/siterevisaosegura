from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from .models import Boleto
import cloudinary.uploader
from datetime import datetime

@login_required
def listar_boletos(request):
    boletos = Boleto.objects.filter(usuario=request.user)
    return render(request, 'boletos/listar_boletos.html', {'boletos': boletos})

@login_required
def detalhar_boleto(request, boleto_id):
    boleto = get_object_or_404(Boleto, id=boleto_id)
    return render(request, 'boletos/detalhar_boleto.html', {'boleto': boleto})

@login_required
def gerar_boleto(request):
    if request.method == "POST":
        valor = request.POST.get("valor")
        vencimento = request.POST.get("vencimento")
        documento = request.FILES.get("documento")

        if not valor or not vencimento:
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
            return redirect("gerar_boleto")

        # 🔹 Upload do documento para o Cloudinary
        documento_url = None
        if documento:
            upload_result = cloudinary.uploader.upload(documento)
            documento_url = upload_result['url']

        boleto = Boleto.objects.create(
            usuario=request.user,
            valor=valor,
            vencimento=vencimento,
            status="pendente",
            documento=documento_url  # 🔹 Salva o link do documento no Cloudinary
        )

        messages.success(request, "Boleto gerado com sucesso!")
        return redirect("listar_boletos")

    return render(request, "boletos/gerar_boleto.html")
