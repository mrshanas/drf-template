FROM python:3.10.6-alpine

LABEL maintainer="mrshanas.me"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements/ /requirements
COPY ./docker/ /docker

RUN chmod +x /docker/run.sh

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /env/bin/pip install -r /requirements/dev.txt && \
    chmod +x /docker/run.sh

COPY . /


ENV PATH="/docker:/env/bin:$PATH"

CMD run.sh
