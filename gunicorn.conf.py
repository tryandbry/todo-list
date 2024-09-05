import os


bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:5000')
accesslog = '-'
wsgi_app = 'app:create_app()'