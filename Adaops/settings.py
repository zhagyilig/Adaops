# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午3:53
# description:


import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# /Users/mac/venv/Adaops
print("BASE_DIR: %s" % BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'q#h)#%gdkxbtr11f=10j5^&n3ruq#1kg$rr3_1)=p9)12)_%4q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # DRF
    'idcs.apps.IdcsConfig',  # IDC
    'users.apps.UsersConfig',  # 用户管理
    'cabinet.apps.CabinetConfig',  # 机柜
    'manufacturers.apps.ManufacturersConfig',  # 服务器厂商
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Adaops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Adaops.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'USER': 'root',
        'PASSWORD': '888888',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
TATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TIME_ZONE = 'Asia/Shanghai'

# 程序日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s:%(lineno)d %(message)s',
            'datefmt': '%Y%m%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'default': {
            'format': '%(asctime)s %(levelname)s  %(name)s %(module)s:%(lineno)d %(message)s',
            'datafme': '%Y%m%d %H:%M:%S',
        }
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            # 'filename': '{}/django.log'.format(os.path.join(BASE_DIR, 'logs')),
            'filename': '/tmp/django.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 20,
        },
        'request': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': '/tmp/django.request.log',
        },
        'server': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': '/tmp/django.server.log',
        },
        'all': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': '/tmp/all.log',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': False,  # 是否向上传递
        },
        'django.request': {
            'handlers': ['request', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['server', ],
            'level': 'DEBUG',
            'propagate': False,
        }

    },
    # 仅接收用户自定义的日志
    'root': {
        'handlers': ['all', ],
        'level': 'DEBUG',
    },
}
