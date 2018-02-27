from djangoblog.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECRET_KEY = os.environ['DJANGO_KEY']
