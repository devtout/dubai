import os, sys
sys.path.append('/home/dubai/apps_wsgi')
os.environ['PYTHON_EGG_CACHE'] = '/home/dubai/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE']='dubai.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
