# Todo List
## Table of Contents
- [Todo List](#todo-list)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Try it out now](#try-it-out-now)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Set Environment Variables](#set-environment-variables)
    - [Database Setup](#database-setup)
    - [Start the app](#start-the-app)
    - [Try it out](#try-it-out)
  - [Local Testing](#local-testing)
    - [Setup](#setup)
    - [Run tests](#run-tests)

## Overview
An API backend for a todo list application.

This app explores the use of the following libraries:
- Flask
- Flask blueprints
- Flask-SQLAlchemy
- Marshmallow

## Try it out now
The API is live on Heroku at [api.todolist.tryandbry.com](https://raw.githack.com/tryandbry/todo-list/main/index.html)!

Try it out now with Swagger UI.

## Getting Started
### Installation
Install dependencies
```
pipenv install
```

### Set Environment Variables
Set environment variables
```
source ./start.sh
```

### Database Setup
Start database
```
docker compose up -d db
```
Migrate database
```
make db.migrate
```
Note: password is `password`

(Alternate procedure) migrate database manually
```
make shell
from lists.models import List
from items.models import Item
from db import db
db.create_all()
```

Seed database
```
make db.seed
```
Note: password is `password`

### Start the app
Start the app
```
make start
```

### Try it out
Health check endpoint: http://localhost:5000/health

Swagger UI: [Todo List API](https://raw.githack.com/tryandbry/todo-list/main/index.html)</br>
Note: Make sure to select `http://localhost:5000` as your server.

## Local Testing
Note: Tests rely on a test database.

### Setup
Set environment variables
```
source ./start.sh
```

Start database
```
docker compose up -d db
```

Create test database
```
make db.test.create
```
Note: Use root password.  Default is `password`

Migrate test database
```
make db.test.migrate
```
Note: Use root password.  Default is `password`

### Run tests
Execute `behave`:
```
make test
```