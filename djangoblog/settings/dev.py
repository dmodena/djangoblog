from djangoblog.settings.base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = config('SECRET_KEY')
