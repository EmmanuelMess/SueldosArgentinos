# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-alpine
EXPOSE 8000

COPY ./requirements.txt /requirements.txt

RUN apk update \
	&& apk add --no-cache python3-dev g++ libc-dev libffi
RUN pip3 install -r requirements.txt --no-cache-dir

RUN addgroup --system docker && adduser --system --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

COPY ./run.sh /run.sh

CMD ["/run.sh"]
