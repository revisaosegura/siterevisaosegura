import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "revisao_segura.settings")

django.setup()

# Rodar migrações automaticamente no início do deploy
call_command("migrate")

application = get_wsgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'revisao_segura.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_default_superuser():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "revisaosegura")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "segurarevisao@gmail.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Admin.2025")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuário '{username}' criado com sucesso!")
    else:
        print(f"Superusuário '{username}' já existe.")

create_default_superuser()

application = get_wsgi_application()
