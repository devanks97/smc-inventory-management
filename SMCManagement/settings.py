import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 't$ct%q$*2h=yegf_yn@1g$a+!^w4s-g3*pcx-nv7$nhrr1nqe%')

DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ["localhost","smc-inventory-management.herokuapp.com","smc-inventory-management-beta.herokuapp.com"]

ADMINS = [('DevanKS', 'devanks97@gmail.com')]
#CHECK IF DEBUG

if DEBUG:

    #DEBUG TOOLBAR CODE STARTS

    from .extraSettings.debug_toolbar_settings import *
    #DEBUG TOOLBAR CODE ENDS

    #LOGGING CODE STARTS

    from .extraSettings.logging_settings import *

    #Logging Code ENDS

#DEBUG EXTRA CODE ENDS

# Application definition

#Installed Apps
from .extraSettings.installedApps import *

#Middleware
from .extraSettings.middleware import *

ROOT_URLCONF = 'SMCManagement.urls'

#Templates

from .extraSettings.templatesSettings import *

WSGI_APPLICATION = 'SMCManagement.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

from .extraSettings.databaseSettings import *

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

from .extraSettings.passwordSettings import *

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


from .extraSettings.staticFilesSettings import *

from .extraSettings.productionLevelChanges import *