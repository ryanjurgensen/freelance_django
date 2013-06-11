from freelance_django.settings import *
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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = '03SM3GWBJ6CWNA8Q7AR2'
AWS_SECRET_ACCESS_KEY = 'e+ps5dGzgaua+4FattqhvZgrVnskyE1jyyfG+gl+iA'
AWS_STORAGE_BUCKET_NAME = 'ryanjurgensen'
MEDIA_URL = 'http://cdn.ryanjurgensen.com/'

