import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'clear_old_codes_every_day': {
        'task': 'accounts.tasks.delete_old_codes',
        'schedule': crontab(minute=0, hour=0),
    },
    'weekly_notify': {
        'task': 'announcements.tasks.regular_subscribers_email_newsletter',
        'schedule': crontab(minute=0, hour=12, day_of_week='sun'),
    }
}
