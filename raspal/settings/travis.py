from . import *

# django appication config
SECRET_KEY = 'qsdgfsghkjghkglkrdtyqsfqsfqsdjdghjfghgb'
DEBUG = False
TRAVIS = True

# django Databases config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_ci_test', 
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configuration SMTP
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True # Configuration a verifier chez votre founisseur de mail
EMAIL_PORT = 587 # Configuration a verifier chez votre founisseur de mail
EMAIL_HOST_USER = 'email@email.com'
EMAIL_HOST_PASSWORD = 'qsfgqdgfqdgfsdfgqgf'
