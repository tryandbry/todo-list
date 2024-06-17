# Todo List
## Overview
An example app exploring the use of:
- Flask
- Flask blueprints
- Flask-SQLAlchemy

## Installation
Install dependencies
```
pipenv install
```

## Quick Start
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

Migrate database (manually)
```
make shell
from lists.models import List
from items.models import Item
from db import db
db.create_all()
```
Note: password is `password`

Seed database
```
make db.seed
```
Note: password is `password`

Start the app
```
make start
```

Try it out: http://localhost:5000
