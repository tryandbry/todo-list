.PHONY: start
start:
	FLASK_APP=app FLASK_ENV=development pipenv run flask run

.PHONY: run
run: start

.PHONY: shell
shell:
	FLASK_APP=app FLASK_ENV=development pipenv run flask shell

.PHONY: db.migrate
db.migrate:
	mysql -u ${MYSQL_USER} -p -h ${MYSQL_HOST} ${MYSQL_DATABASE} < db/migrate.sql

.PHONY: db.seed
db.seed:
	mysql -u ${MYSQL_USER} -p -h ${MYSQL_HOST} ${MYSQL_DATABASE} < db/seed.sql
