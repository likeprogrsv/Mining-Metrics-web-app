FROM python:3.8.10-alpine3.14

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY . .

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /app/static && \
    chown -R app:app /vol && \
    chmod -R 755 /vol
        
ENV PATH="/scripts:/py/bin:$PATH"

USER app

