import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config, Csv
import dj_database_url
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import logging

# Carregar variáveis do .env
load_dotenv()

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Configuração do Django
SECRET_KEY = config("DJANGO_SECRET_KEY", default="fallback_key_should_be_removed")
DEBUG = False
ALLOWED_HOSTS = ["www.revisaosegura.com.br", "revisaosegura.com.br", "127.0.0.1", "localhost", "siterevisaosegura.onrender.com"]
ROOT_URLCONF = "revisao_segura.urls"

# 🔹 Configuração do Banco de Dados PostgreSQL
DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://revisao_user:wReqJqaDOzMkVy8uayvgjywRFblPQOwx@dpg-d0n2itt6ubrc73a1mhkg-a.oregon-postgres.render.com/revisao'
    )
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
    'django_extensions',
    'cloudinary',
    'cloudinary_storage',
    'rest_framework',

    # Aplicativos internos
    'revisao_segura.usuarios',
    'revisao_segura.boletos',
    'revisao_segura',
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
LOGIN_URL = '/usuarios/login.html/'
LOGIN_REDIRECT_URL = '/usuarios/dashboard.html/'
LOGOUT_REDIRECT_URL = '/usuarios/login.html/'

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
    cloud_name = "dzzccricy", 
    api_key = "614811795386991", 
    api_secret = "rGYrmZ31oTC_3wUWP_ZXIgHmETk", # Click 'View API Keys' above to copy your API secret
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

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
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'contato@revisaosegura.com.br' # ou o e-mail que você usa no Zoho
EMAIL_HOST_PASSWORD = '8YGnRdqRkJYC'  # senha real ou senha de aplicativo
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)
