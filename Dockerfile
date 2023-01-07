# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM builder as dev-envs

RUN addgroup --system docker && adduser --system --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
