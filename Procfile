web: gunicorn battlecat.wsgi --log-file -
worker: celery -A battlecat worker -l info
beat: celery -A battlecat beat -l info
