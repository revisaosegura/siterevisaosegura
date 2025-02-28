import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "revisao_segura.settings")
django.setup()

from django.core.management import call_command
call_command("migrate")  # Roda as migrações automaticamente

application = get_asgi_application()
