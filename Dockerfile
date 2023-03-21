FROM python:3.11.2 as setup
RUN mkdir -p /usr/src
WORKDIR /usr/src
COPY Pipfile .
RUN pipenv run install
COPY . .
