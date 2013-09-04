from freelance_django.settings import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = True
DEV = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'freelance',                 
        'USER': 'root',                      
        'PASSWORD': 'root',               
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock', 
        'PORT': '', 
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(os.path.join(PROJECT_ROOT, 'templates')),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'log.txt'),
            'maxBytes': 500000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'sqllogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, "sqllog.txt"),
            'maxBytes': 50000000,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['sqllogfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}