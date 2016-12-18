from __future__ import absolute_import

import os
import sys

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example_project.settings')
sys.path.insert(0, '/Users/adam/Projects/battlecat')

from django.conf import settings  # noqa

app = Celery('proj')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

