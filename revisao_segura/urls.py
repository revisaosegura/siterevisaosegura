from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from revisao_segura.views import home, sobre, contato, upload_documento, calculo_view, servicos, simulacao_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('usuarios/', include ('revisao_segura.usuarios.urls')),
    path('boletos/', include ('revisao_segura.boletos.urls')),
    path('upload/', upload_documento, name='upload_documento'),
    path('calculo/', calculo_view, name='calculo'),
    path('servicos/', servicos, name='servicos'),
    path('solicitar-calculo/', calculo_view, name='solicitar_calculo'),
    path('simule/', simulacao_view, name='simulacao'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos estáticos e de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
