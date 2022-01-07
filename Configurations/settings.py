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
    'Users',
    'Administration',
]

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

# Configurações de CORS do sistema
CORS_ORIGIN_ALLOW_ALL = False # Não permite acessso de todos os domínios
CORS_ORIGIN_WHITELIST = (
    'http://lochhost:3000', # Quem pode acessar seus domínios
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
