import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecobin_backend.settings')

app = Celery('ecobin_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()