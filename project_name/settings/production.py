from .base import *

import dj_database_url

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# https://github.com/jacobian/dj-database-url

DATABASES = {
    'default': dj_database_url.config(
        default = config('DATABASE_URL')
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST') 
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True