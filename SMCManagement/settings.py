import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 't$ct%q$*2h=yegf_yn@1g$a+!^w4s-g3*pcx-nv7$nhrr1nqe%')

DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ["localhost",os.environ.get('HEROKU_ALLOWED_HOST')]

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

from .extraSettings.templatesSettings import *

WSGI_APPLICATION = 'SMCManagement.wsgi.application'

from .extraSettings.databaseSettings import *

from .extraSettings.passwordSettings import *

from .extraSettings.internationalizationSettings import *


from .extraSettings.staticFilesSettings import *

from .extraSettings.productionLevelChanges import *