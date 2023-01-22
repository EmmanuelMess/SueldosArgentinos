# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-slim

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir
