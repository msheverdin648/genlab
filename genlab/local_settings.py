import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


SECRET_KEY = 'ev(ff%cju_=mgqi5=6sj-kwv_3t!llgf+drp@+lw5p=hp2a&s5'

DEBUG = True

ALLOWED_HOSTS = ['.pythonanywhere.com', '127.0.0.1']




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_DIR = os.path.join(PROJECT_ROOT, 'static')
STATICFIELS_DIRS = (
    os.path.join(PROJECT_ROOT, 'static')
     )
STATIC_ROOT =  os.path.join(PROJECT_ROOT, 'static')