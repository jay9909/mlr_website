# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
SUDO apt-get install wget

./sqlproxy.sh
./dev_runner.sh -s