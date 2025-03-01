import os
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta do Django
SECRET_KEY = 'Revisaosegura.2025'

# Ativar modo de depuração (Apenas para desenvolvimento)
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = [
    "siterevisaosegura.onrender.com",  # Domínio do Render
    "127.0.0.1",  # Para testes locais
    "localhost"   # Para rodar localmente
    "revisaosegura.com.br",
    "www.revisaosegura.com.br",
]
APPEND_SLASH = True

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",

   
    # Aplicativos internos
    'revisao_segura.usuarios',  # ⚠️ Certifique-se de que está assim!
    'revisao_segura.boletos',

    # Bibliotecas externas
    'rest_framework',  # API
]

# Middlewares
MIDDLEWARE = [
    "revisao_segura.middleware.WWWRedirectMiddleware",  # Adicione essa linha
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Adicione esta linha
]

# Configuração de URLs
ROOT_URLCONF = 'revisao_segura.urls'

# Configuração dos Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Caminho correto para templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do WSGI
WSGI_APPLICATION = 'revisao_segura.wsgi.application'

# Configuração do banco de dados (SQLite)
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',  # Correção do caminho
        }
    }

# Configuração de autenticação e senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuração do modelo de usuário personalizado
AUTH_USER_MODEL = 'usuarios.Usuario'

# Configuração de URLs de autenticação
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Configuração de idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuração de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = str(BASE_DIR / 'staticfiles')  # Convertendo para string

# Configuração de arquivos de mídia (uploads de documentos e contratos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuração do Django Rest Framework (DRF) para APIs
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Configuração de envio de e-mails para redefinição de senha
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Configurar para o seu provedor de e-mail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@gmail.com'  # Configurar com seu e-mail
EMAIL_HOST_PASSWORD = 'sua_senha'  # Configurar com sua senha
DEFAULT_FROM_EMAIL = 'Revisão Segura <noreply@seusite.com>'

GERENCIANET_CREDENTIALS = {
    "client_id": "SUA_CLIENT_ID",
    "client_secret": "SUA_CLIENT_SECRET",
    "sandbox": True,  # Defina como False para ambiente de produção
    "cert_path": "caminho/do/seu/certificado.pem"
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ["https://www.revisaosegura.com.br", 'https://siterevisaosegura.onrender.com']

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SESSION_ENGINE = "django.contrib.sessions.backends.db"  # Usa banco de dados para sessões
SESSION_COOKIE_SECURE = False  # Se estiver em HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = 86400
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


