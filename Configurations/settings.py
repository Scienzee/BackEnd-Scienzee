from pathlib import Path
import os, sys


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(
    os.path.join(BASE_DIR, "Applications")
)


SECRET_KEY = 'django-insecure-8=t@r6%%nri%@d7-0de*p#3yq6w5l63v1$e13v^^x0&cij7v+k'
DEBUG = True
ALLOWED_HOSTS = []


# Aplicações internas do Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Aplicações externas do Django
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
    'rest_auth.registration', 
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.google', 
    'Users',
    'Administration',
    'Relations',
    'ckeditor',
    'ckeditor_uploader',
]


CKEDITOR_UPLOAD_PATH = "uploads/"

SITE_ID = 1

# MIDDLEWARE interno do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# MIDDLEWARE externo do Django
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

# Configurando configurações de usuários 

# Declarando qual é o novo padrão de User
AUTH_USER_MODEL = "Users.User" 

# Redirecionando para a pagina inicial depois de logar
# LOGIN_REDIRECT_URL = 'ViewIndex' 

# Definindo a view padrão do Django de login
# LOGIN_URL = 'ViewLogin' 

# Configurações de CORS do sistema
CORS_ORIGIN_ALLOW_ALL = True # Permite acessso de todos os domínios
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000', # Quem pode acessar seus domínios
)




ROOT_URLCONF = 'Configurations.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Configurations.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True



STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
# MEDIA_ROOT é para o caminho do servidor para armazenar arquivos no computador.
MEDIA_URL = '/media/'
# MEDIA_URL é o URL de referência para o navegador acessar os arquivos via Http.


