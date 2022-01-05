from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')

app = Celery('Yektanet')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-hour-click': {
        'task': 'periodic_tasks.tasks.clickHourly',
        'schedule': crontab(hour='*/1', minute=0)
    },
    'every-hour-view': {
        'task': 'periodic_tasks.tasks.viewHourly',
        'schedule': crontab(hour='*/1', minute=0)
    },
    'every-day-click': {
        'task': 'periodic_tasks.tasks.clickDaily',
        'schedule': crontab(hour=0, minute=0)
    },
    'every-day-view': {
        'task': 'periodic_tasks.tasks.viewDaily',
        'schedule': crontab(hour=0, minute=0)
    }
}

app.conf.timezone = 'Asia/Tehran'

app.autodiscover_tasks()
