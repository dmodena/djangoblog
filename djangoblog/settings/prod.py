from djangoblog.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['infinite-island-95788.herokuapp.com']
SECRET_KEY = os.environ['DJANGO_KEY']
