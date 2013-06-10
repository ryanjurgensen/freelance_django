from dynamo.settings import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = True

DEV = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'freelance',
        'USER': 'freelance',
        'PASSWORD': 'freelance', 
        'HOST': 'freelance.c6usmdzxajjd.us-west-2.rds.amazonaws.com', 
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = '/media/'

