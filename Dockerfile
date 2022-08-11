FROM python:3.8.13-alpine3.14

COPY . /boxticket

WORKDIR /boxticket

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add gcc libffi-dev openssl-dev g++ musl-dev
RUN apk add postgresql-client

RUN pip install --upgrade pip
RUN pip install -r requirements/base.txt

EXPOSE 8000
RUN chmod +x wait-for-postgres.sh