FROM python:3.12.5-alpine

RUN apk add make
RUN pip install pipenv
RUN mkdir /app
WORKDIR /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN pipenv install
COPY . /app

EXPOSE 5000

CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
