from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from revisao_segura.views import home, sobre, contato, upload_documento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('usuarios/', include ('revisao_segura.usuarios.urls')),
    path('boletos/', include ('revisao_segura.boletos.urls')),
    path('upload/', upload_documento, name='upload_documento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos estáticos e de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
