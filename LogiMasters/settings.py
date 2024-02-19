"""
Django settings for LogiMasters project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ce_%5(uv5n@d6m7ap*hp6bh^tvps&^)1p%nt55og7&6di+_pwa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['logimasterssilicon.onrender.com','*']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.gis',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fleet',
    'Users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://logimasterssilicon.onrender.com",
    "https://logimasterssilicon.onrender.com",
    # Add more allowed origins as needed
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGIN= True


CORS_ORIGIN_WHITELIST = [
    'http://logimasterssilicon.onrender.com',
    "https://logimasterssilicon.onrender.com",
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Encoding',
    'Authorization',
    'Content-Type',
    'Origin',
    'Referer',
    'User-Agent',
]

ROOT_URLCONF = 'LogiMasters.urls'

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

# WSGI_APPLICATION = 'LogiMasters.wsgi.application'
ASGI_APPLICATION = 'LogiMasters.asgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES={
#     'default':dj_database_url.parse("postgres://logimasters_user:gyGXdciIp6Hd7c9e9kpMZhQP4dsWIDlU@dpg-cn5qko7109ks73a0coog-a/logimasters")
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'logimasters',
#         'USER': 'postgres',
#         'PASSWORD': '21beeb10',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES["default"]=dj_database_url.parse("postgres://logimasters_user:gyGXdciIp6Hd7c9e9kpMZhQP4dsWIDlU@dpg-cn5qko7109ks73a0coog-a.oregon-postgres.render.com/logimasters")


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'Users.FleetManagers'


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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import redis

# Your existing Redis client setup
r = redis.Redis(
    host='redis-14911.c264.ap-south-1-1.ec2.cloud.redislabs.com',
    port=14911,
    password='IFJCEfrs5nuXae8a8wEwhy0DfR5cLYyZ')

# Configure Django Channels to use the existing Redis client
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [f"redis://:{r.connection_pool.connection_kwargs['password']}@{r.connection_pool.connection_kwargs['host']}:{r.connection_pool.connection_kwargs['port']}"],
        },
    },
}


TWILIO_ACCOUNT_SID = 'AC85e2d8698a5e8d51bb77316ea445648e'
TWILIO_AUTH_TOKEN = 'a58dcf4629f2bcfda3fcf2e89dfe845d'
TWILIO_PHONE_NUMBER = '+16593335075'  # Should be in the format '+1234567890'


# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

