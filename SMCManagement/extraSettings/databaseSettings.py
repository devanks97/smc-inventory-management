# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

import os
from ..settings import BASE_DIR
DATABASES = {
#LOCAL DATABASE
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'localDb.sqlite3'),
    }
}
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
IMPORT_EXPORT_USE_TRANSACTIONS = True