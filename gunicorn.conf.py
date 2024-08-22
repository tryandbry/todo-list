import os


bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:5000')
