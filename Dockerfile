FROM python:3.8-slim

RUN mkdir -p ./djangoRestApp

WORKDIR ./djangoRestApp

COPY . /djangoRestApp

RUN apt update

RUN apt install python3 -y

RUN pip install -r requirements.txt
