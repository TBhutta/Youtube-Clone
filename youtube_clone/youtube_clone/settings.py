from pathlib import Path

# from django.conf.global_settings import LOGIN_URL
from dotenv import load_dotenv
import os
from os import getenv
# from django.forms.renderers import TemplatesSetting
# import django.forms as forms


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&))7qbhbrp8^$vwri+71dtl1(srxwv111l61--49-^%vp^tpwv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = "authentication.Account"
# LOGIN_URL = "authentication/sign-in"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
    "authentication",
    "channel",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "youtube_clone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "youtube_clone.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.postgresql",
        # "NAME": os.environ.get("DB_NAME"),
        # "USER": os.environ.get("USERNAME"),
        # "PASSWORD": os.environ.get("PASSWORD"),
        # "HOST": os.environ.get("HOST"),
        # "PORT": os.environ.get("PORT"),

        'NAME': getenv('PGDATABASE'),
        'USER': getenv('PGUSER'),
        'PASSWORD': getenv('PGPASSWORD'),
        'HOST': getenv('PGHOST'),
        'PORT': getenv('PGPORT', 5432),
        'OPTIONS': {
            'sslmode': 'require',
        },
        'DISABLE_SERVER_SIDE_CURSORS': True,
        'CONN_HEALTH_CHECKS': True,

    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [BASE_DIR, os.path.join(BASE_DIR, 'static')]

# FILE_UPLOAD_HANDLERS = [
#     "django.core.files.uploadhandler.MemoryFileUploadHandler",
#     "django.core.files.uploadhandler.TemporaryFileUploadHandler",
# ]



AWS_ACCESS_KEY_ID = getenv('B2_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('B2_APPLICATION_KEY')
AWS_STORAGE_BUCKET_NAME = getenv('B2_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('B2_ENDPOINT')
AWS_S3_REGION_NAME = os.getenv('B2_REGION')


# Security settings for Private Bucket
AWS_S3_ADDRESSING_STYLE = "path"
AWS_QUERYSTRING_AUTH = True  # Generates temporary signed links
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False # Prevents deleting files with same name

if AWS_STORAGE_BUCKET_NAME:
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }


    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'


# class CustomFormRenderer(TemplatesSetting):
#     form_template_name = "formTemplate.html"

# class MyForm(forms.Form):
#     template_name = "formTemplate.html"


# FORM_RENDERER = "youtube_clone.settings.CustomFormRenderer"