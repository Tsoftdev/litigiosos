"""
Django settings for paymentintegration project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+%)!&%m6e9d9m^&_)+ks@c&#a6b95+$#bcd$#)e#ln%#%_jm5)'

# Application definition

INSTALLED_APPS = [
    'cities_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'payments_mercadopago',
    'paymentintegration.authentication',
    # 'paymentintegration.djangomerchapago',
    # 'paymentintegration.paymerchapago',
    'import_export',
    'dal',
    'dal_select2',
    'paymentintegration.website',
    'paymentintegration.land',
    'paymentintegration.administrate',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]
#clientID='757652617283-sko8iueol1voctvgsvdov32ooptq12a0.apps.googleusercontent.com'
#clientSecret='mD5JIHwPBOfySuFv0pnZGVb-'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = [
    'paymentintegration.authentication.authenticatebackend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    }
}

ROOT_URLCONF = 'paymentintegration.urls'

AUTH_USER_MODEL = 'authentication.User'

PAYMENT_HOST = '*'
PAYMENT_USES_SSL = False
PAYMENT_MODEL = 'website.Payment'
PAYMENT_VARIANTS = {
    'MercadoPago':('payments_mercadopago.MercadoPagoProvider',{
        'access_token': 'MERCADO_PAGO_SANDBOX_ACCESS_TOKEN',
        'sandbox_mode': True})
}

CHECKOUT_PAYMENT_CHOICES = [('MercadoPago', 'Mercado Pago')]

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

WSGI_APPLICATION = 'paymentintegration.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

ACCOUNT_ACTIVATION_DAYS = 7

# Email section
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'AKIAX2S4VVGRW7MNVLUQ'
EMAIL_HOST_PASSWORD = 'BB5h+7zUMazc+YsLTxQOkjvJbZpJin04ClwZgs22oXGZ'
EMAIL_USE_SSL = True
# EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL = 'contacto@litigiosos.com'

CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr', 'en', 'de', 'pt', 'it', 'zh-hans', 'es']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT',]

try:
    from .djmercadopago_settings import *
except ImportError as e:
    print("#`djmercadopago_sample_app_settings`")
    raise Exception("Couldn't import 'djmercadopago_sample_app_settings'")

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home/coonsultorio/litigiosos/colectstatic/"
STATICFILES_DIRS = (
    BASE_DIR / "static",
)

LOGIN_REDIRECT_URL = 'land'

LOGIN_URL = 'view_login'

LOGOUT_REDIRECT_URL = 'view_login'
