import requests
from django.conf import settings

def gerar_boleto(nome, email, cpf, valor):
    credentials = settings.GERENCIANET_CREDENTIALS

    url = "https://api.gerencianet.com.br/v1/charge"

    headers = {
        "Authorization": f"Bearer {credentials['client_id']}",
        "Content-Type": "application/json"
    }

    payload = {
        "items": [
            {
                "name": "Revisão de Juros",
                "value": int(valor * 100),  # Convertendo para centavos
                "amount": 1
            }
        ],
        "customer": {
            "name": nome,
            "email": email,
            "cpf": cpf
        }
    }

    print(f"Enviando requisição para {url} com payload: {payload}")  # ✅ Debug

    response = requests.post(url, json=payload, headers=headers)

    print(f"Status Code: {response.status_code}")  # ✅ Verificar se a API responde corretamente
    print(f"Resposta da API: {response.text}")  # ✅ Verificar se há mensagem de erro

    if response.status_code == 201:
        return response.json()  # Retorna os dados do boleto
    else:
        return response.text  # Retorna a mensagem de erro para depuração
