import os 
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-361-xu3ulze(w-^in0td3h6y^7ofku#iy8%=-9rv%2ci%r$67)'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS += [ 
    'debug_toolbar',
]

MIDDLEWARE += [ 
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [ 
    '127.0.0.1',
]

cwd = os.getcwd()

CACHES = {
    "default":{
        "BACKEND":
        "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION" : f"{cwd}/.cache"
    }
}

# try:
#     from .local import *
# except ImportError:
#     pass
