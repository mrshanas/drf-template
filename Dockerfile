FROM python:3.10.6-alpine
LABEL maintainer="mrshanas.com"

ENV PYTHONUNBUFFERED=1

COPY ./requirements/dev.txt /requirements/dev.txt
COPY ./requirements/prod.txt /requirements/prod.txt
COPY ./docker/run.sh /docker/run.sh

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements/prod.txt && \
    chmod +x /docker/run.sh


# COPY ./docker/
COPY . ./

ENV PATH="/docker:/py/bin:$PATH"

CMD run.sh