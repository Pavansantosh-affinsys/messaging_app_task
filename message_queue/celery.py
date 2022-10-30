from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "message_queue.settings")
app = Celery("message_queue")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.enable_utc = False
app.conf.update(timezone=settings.CELERY_TIMEZONE)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
