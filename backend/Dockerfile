FROM python:3.7.4-alpine

LABEL author="Marcus Pereira <oi@spacedevs.info>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .