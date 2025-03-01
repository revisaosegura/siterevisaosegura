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

def reset_admin_password():
    User = get_user_model()
    username = "revisaosegura"  # Substitua pelo seu usuário admin
    new_password = "Admin.2025"  # Nova senha

    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        print(f"Senha do superusuário '{username}' foi redefinida com sucesso!")
    except User.DoesNotExist:
        print(f"O usuário '{username}' não existe.")

reset_admin_password()

application = get_wsgi_application()
