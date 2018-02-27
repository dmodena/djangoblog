from djangoblog.settings.base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['infinite-island-95788.herokuapp.com']
SECRET_KEY = os.environ['DJANGO_KEY']
DATABASES['default'] = dj_database_url.config()
