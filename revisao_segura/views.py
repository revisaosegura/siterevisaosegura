from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import cloudinary.uploader

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        celular = request.POST.get("celular")
        mensagem = request.POST.get("mensagem")

        if not nome or not email or not mensagem:
            messages.error(request, "Todos os campos são obrigatórios!")
            return redirect("contato")  # Redireciona para a página de contato

        # Aqui você pode adicionar lógica para enviar email ou salvar a mensagem no banco

        messages.success(request, "Sua mensagem foi enviada com sucesso! Responderemos em breve.")
        return redirect("contato")  # Redireciona para evitar reenvio do formulário

    return render(request, "contato.html")

def calculo_view(request):
    if request.method == 'POST':
        # você pode personalizar isso depois
        messages.success(request, 'Solicitação enviada com sucesso!')
        return redirect('calculo')  # ou outra URL
    return render(request, 'calculo.html')

def servicos(request):
    return render(request, 'servicos.html')

def upload_documento(request):
    if request.method == 'POST' and request.FILES.get('file'):
        arquivo = request.FILES['file']
        resultado = cloudinary.uploader.upload(arquivo)
        return JsonResponse({'url': resultado['secure_url']})

    return JsonResponse({'error': 'Nenhum arquivo enviado'}, status=400)
