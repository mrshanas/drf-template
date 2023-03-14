FROM python:3.10.6-alpine

LABEL maintainer="nassibshaban345@gmail.com"

# setup work directory


# set up environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements/ /requirements
COPY ./compose/production/django/scripts/ /scripts

# install psycopg2 dependencies
RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /env/bin/pip install -r /requirements/prod.txt 

RUN chmod +x /scripts/entrypoint.sh

COPY . /

ENV PATH="/scripts:/env/bin:$PATH"

# run entrypoint.sh
CMD [ "/scripts/entrypoint.sh" ]
