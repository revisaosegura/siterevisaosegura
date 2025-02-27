from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from revisao_segura.boletos.models import Boleto
from django.contrib import messages
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import date
from django.urls import reverse
from .models import Boleto
from django.shortcuts import get_object_or_404, render
from datetime import datetime, timedelta

@login_required
def listar_boletos(request):
    boletos = Boleto.objects.filter(usuario=request.user)
    return render(request, 'boletos/listar_boletos.html', {'boletos': boletos})

@login_required
def detalhar_boleto(request, boleto_id):
    boleto = get_object_or_404(Boleto, id=boleto_id)
    return render(request, 'boletos/detalhar_boleto.html', {'boleto': boleto})

def gerar_boleto(request):
    if request.method == "POST":
        valor = request.POST.get("valor")

        if not valor:
            messages.error(request, "Por favor, insira um valor válido para o boleto.")
            return redirect("gerar_boleto")

        boleto = Boleto.objects.create(
            usuario=request.user,
            valor=valor,
            data_vencimento="dd/mm/yyyy",
            status="pendente"
        )
        
        messages.success(request, "Boleto gerado com sucesso!")
        return redirect("listar_boletos")

    url = reverse('gerar_boleto', args=[boleto.id])

    return render(request, "boletos/gerar_boleto.html")

def gerar_boleto(request, boleto_id):
    boleto = get_object_or_404(Boleto, id=boleto_id)
    return render(request, 'boletos/gerar_boleto.html', {'boleto': boleto})


