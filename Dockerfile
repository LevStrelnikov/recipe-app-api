FROM python:3.7-alpine
MAINTAINER Lev Strelnikov

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirments.txt
RUN pip install -r /requirments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
