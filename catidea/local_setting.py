import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.path.join(BASE_DIR, 'db.postgresql'),
    }
}

ALLOWED_HOSTS = []

DEBUG = True
