import os

bind = os.environ.get('PORT', '5000')
accesslog = '-'
wsgi_app = 'app:create_app()'
