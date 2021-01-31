import os

DEBUG = int(os.environ.get("DEBUG", default=0))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rbapi',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '192.168.0.108',
        'PORT': '5432',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "django"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "django"),
#         "HOST": os.environ.get("SQL_HOST", "db"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "rbapi/static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Keys and Hosts
API_KEY = 'qwerty-12345'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
SECRET_KEY = 'lob2t$8)n*-lh#40k7$d5v(y4vlm1%v%q_%ci261^g=q)(!--c'

# SECRET_KEY = os.environ.get("SECRET_KEY")
# API_KEY = os.environ.get("API_KEY")
# DEBUG = int(os.environ.get("DEBUG", default=0))
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")



