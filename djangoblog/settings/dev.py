from djangoblog.settings.base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = config('SECRET_KEY')
