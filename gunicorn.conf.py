# will use 0.0.0.0:$PORT if $PORT is defined
# i.e. define a $PORT env variable
accesslog = '-'
wsgi_app = 'app:create_app()'
