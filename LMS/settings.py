"""
Django settings for LMS project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import datetime
import os
import dotenv

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "LOAN",
    "storages",
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

ROOT_URLCONF = "LMS.urls"

CORS_ALLOW_HEADERS = "*"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "LMS.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["DATABASE_NAME"],  # database table name
        "HOST": os.environ[
            "DATABASE_HOST"
        ],  # Or an IP Address that your DB is hosted on
        "USER": os.environ["DATABASE_USER"],  # databases user name
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "PORT": "3306",
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


DATE_INPUT_FORMATS = ["%d/%m/%Y"]


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]


if not DEBUG:
    DEFAULT_FILE_STORAGE = os.environ["DEFAULT_FILE_STORAGE"]
    STATICFILES_STORAGE = os.environ["STATICFILES_STORAGE"]
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_FILE_EXPIRE = os.environ["AWS_FILE_EXPIRE"]
    AWS_PRELOAD_METADATA = os.environ["AWS_PRELOAD_METADATA"]
    AWS_QUERYSTRING_AUTH = os.environ["AWS_QUERYSTRING_AUTH"]
    AWS_DEFAULT_ACL = os.environ["AWS_DEFAULT_ACL"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_FILE_OVERWRITE = os.environ["AWS_S3_FILE_OVERWRITE"]
    AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]
    AWS_S3_SIGNATURE_VERSION = os.environ["AWS_S3_SIGNATURE_VERSION"]
    DEFAULT_FILE_STORAGE = os.environ["DEFAULT_FILE_STORAGES"]
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.0/howto/static-files/

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "assets")
    # STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    # STATICFILES_DIRS = [BASE_DIR / "static"]
