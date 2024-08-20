.PHONY: start
start:
	FLASK_APP=app FLASK_ENV=development pipenv run flask run

.PHONY: run
run: start

.PHONY: shell
shell:
	FLASK_APP=app FLASK_ENV=development pipenv run flask shell

.PHONY: test
test:
	pipenv run behave --no-capture --no-color --no-skipped --tags=wip

.PHONY: test.all
test.all:
	pipenv run behave

.PHONY: db.start
db.start:
	docker compose up -d db

.PHONY: db.stop
db.stop:
	docker compose down db

.PHONY: db.migrate
db.migrate:
	mysql -u ${MYSQL_USER} -p -h ${MYSQL_HOST} ${MYSQL_DATABASE} < db/migrate.sql

.PHONY: db.seed
db.seed:
	mysql -u ${MYSQL_USER} -p -h ${MYSQL_HOST} ${MYSQL_DATABASE} < db/seed.sql

.PHONY: db.client
db.client:
	mysql -u ${MYSQL_USER} -p -h ${MYSQL_HOST} ${MYSQL_DATABASE}

.PHONY: db.dump
db.dump:
	mysqldump -h ${MYSQL_HOST} -u root -p ${MYSQL_DATABASE} > db/todo.sql

.PHONY: db.test.create
db.test.create:
	mysql -u root -h ${MYSQL_HOST} -p < db/test_setup.sql

.PHONY: db.test.migrate
db.test.migrate:
	mysql -u ${MYSQL_USER} -h ${MYSQL_HOST} -p ${TEST_MYSQL_DATABASE} < db/migrate.sql
