#!/bin/bash

export FLASK_APP=app
export FLASK_ENV=development
export SECRET_KEY=`tr -dc A-Za-z0-9 </dev/urandom | head -c 128`
export MYSQL_DATABASE=todo
export MYSQL_USER=app
export MYSQL_PASSWORD=password
export MYSQL_HOST=127.0.0.1
export DATABASE_URI="mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}/${MYSQL_DATABASE}"
