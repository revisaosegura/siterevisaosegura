import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "revisao_segura.settings")
django.setup()

from django.core.management import call_command
call_command("migrate")  # Roda as migrações automaticamente

application = get_wsgi_application()
