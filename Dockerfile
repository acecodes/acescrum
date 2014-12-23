# Proper build for Django
FROM ubuntu:14.04
MAINTAINER Ace Eddleman <ace.github@gmail.com>
RUN apt-get update && apt-get install python3.4 python-pip -y
RUN pip install django djangorestframework psycopg2 requests django-filter Markdown