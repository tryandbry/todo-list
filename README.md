# Todo List
## Table of Contents
- [Todo List](#todo-list)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Try it out now](#try-it-out-now)
  - [Local Development Quick Start](#local-development-quick-start)
  - [Testing](#testing)
    - [Setup](#setup)
    - [Run tests](#run-tests)

## Overview
An example app exploring the use of:
- Flask
- Flask blueprints
- Flask-SQLAlchemy
- Marshmallow

## Installation
Install dependencies
```
pipenv install
```

## Try it out now
[Swagger UI](https://raw.githack.com/tryandbry/todo-list/feature/ssl/index.html)

## Local Development Quick Start
Set environment variables
```
source ./start.sh
```

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

Start the app
```
make start
```

Try it out: http://localhost:5000/health

## Testing
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