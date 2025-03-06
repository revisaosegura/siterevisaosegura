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

call_command('migrate')
print("Migrações aplicadas com sucesso!")

application = get_wsgi_application()

os.makedirs("/tmp/media", exist_ok=True)

