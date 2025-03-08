import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config, Csv
import dj_database_url
import cloudinary
import cloudinary.api
import cloudinary.uploader

# Carregar variáveis do .env
load_dotenv()

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Configuração do Django
SECRET_KEY = config("DJANGO_SECRET_KEY", default="fallback_key_should_be_removed")
DEBUG = config("DEBUG", default=False, cast=lambda v: v.lower() in ("true", "1"))
ALLOWED_HOSTS = ["www.revisaosegura.com.br", "revisaosegura.com.br", "127.0.0.1", "localhost"]
ROOT_URLCONF = "revisao_segura.urls"

# 🔹 Configuração do Banco de Dados PostgreSQL
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Debug: Mostrar a configuração do banco
print(f"🚀 CONFIG FINAL DATABASES: {DATABASES}")

# 🔹 Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'rest_framework',

    # Aplicativos internos
    'revisao_segura.usuarios',
    'revisao_segura.boletos',
]

# 🔹 Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# 🔹 Configuração dos Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 🔹 Configuração do WSGI
WSGI_APPLICATION = 'revisao_segura.wsgi.application'

# 🔹 Configuração de autenticação
AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# 🔹 Configuração de linguagem e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 🔹 Configuração de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# 🔹 Configuração do Cloudinary
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = f"https://res.cloudinary.com/{config('CLOUDINARY_CLOUD_NAME')}/"

# 🔹 Configuração do Django Rest Framework (DRF)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# 🔹 Configuração de envio de e-mails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='seu_email@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='sua_senha')
DEFAULT_FROM_EMAIL = 'Revisão Segura <noreply@seusite.com>'

# 🔹 Configuração de segurança
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# 🔹 Configuração de sessões
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = 86400  # 1 dia
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# 🔹 Configuração de mensagens do Django
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# 🔹 Debug para confirmar carregamento
print("✅ Configuração do settings.py carregada com sucesso!")
