"""
Django settings for unistock project.

Use for production

"""

from pathlib import Path

# || Base project directory (root)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# || SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k!awc52w$bkb9tj($myyoo5%p=i59n0)8xyrsp(nn08l^a44iv'

# || Debug options for development/production
DEBUG = False

# Allowed hosts for project
ALLOWED_HOSTS = ['unistock.online', 'www.unistock.online']


# || Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.core'
]

# || Middleware options
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# || Root url configuration file
ROOT_URLCONF = 'config.urls'

# || Template directory options
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
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

# || WSGI app location
WSGI_APPLICATION = 'config.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# || Password validation
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


# || Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# || Static files (CSS, JavaScript, Images)

# Static
STATIC_URL = '/static/'
STATIC_ROOT = 'apps/core/static'

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = 'apps/core/static/core/media/'

# || Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
