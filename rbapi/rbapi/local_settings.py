import os

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rbapi',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

API_KEY = 'qwerty-12345'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'ec2-18-196-1-11.eu-central-1.compute.amazonaws.com', '18.196.1.11']

SECRET_KEY = 'lob2t$8)n*-lh#40k7$d5v(y4vlm1%v%q_%ci261^g=q)(!--c'

STATIC_ROOT = os.path.join(BASE_DIR, "/static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
