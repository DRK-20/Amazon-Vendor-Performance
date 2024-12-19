"""
Django settings for vendor_performance project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# **Note:** It's highly recommended to change this key to a unique, unpredictable value for production.
SECRET_KEY = 'django-insecure-3k#b13_+6*z7vsiqn+otcb8qun5w!gqiqvscu4@8+*z*0en$_+'  # Replace with your actual secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = []  # Add your domain names or IP addresses in production, e.g., ['yourdomain.com', 'www.yourdomain.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'registrations',
    'product_viewing',
    'analysis_genai',
    'scraper',
    'landing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vendor_performance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Added the 'templates' directory at the project root
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # Looks for templates inside each app's 'templates' directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by Django's admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vendor_performance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Using SQLite for development; consider PostgreSQL or another robust DB for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},  # Enforce a minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Additional directories where Django will search for static files
STATICFILES_DIRS = [BASE_DIR / 'static']

# The absolute path to the directory where collectstatic will collect static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------
# User Authentication Settings
# -------------------------------

# Redirect users to the dashboard after successful login
LOGIN_REDIRECT_URL = 'dashboard'

# Redirect users to the login page after logout
LOGOUT_REDIRECT_URL = 'login'

# -------------------------------
# Additional Security Settings
# -------------------------------

# **Note:** The following settings should be enabled when deploying to production to enhance security.

# Uncomment and set to True in production
# DEBUG = False

# Example of setting allowed hosts in production
# ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Use secure cookies
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Enable HTTP Strict Transport Security (HSTS)
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Redirect all non-HTTPS requests to HTTPS
# SECURE_SSL_REDIRECT = True

# Content Security Policy, etc.
# Add additional security settings as needed
