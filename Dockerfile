FROM python:3.7-alpine AS base

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

FROM base AS deploy

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user

FROM base AS test

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./requirements-dev.txt /requirements-dev.txt
RUN pip install -r /requirements-dev.txt

RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user
