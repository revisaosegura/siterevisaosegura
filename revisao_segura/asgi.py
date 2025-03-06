import os
import django
from django.core.asgi import get_asgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "revisao_segura.settings")

django.setup()

call_command("migrate")  # Roda as migrações automaticamente

application = get_asgi_application()

os.makedirs("/tmp/media", exist_ok=True)
