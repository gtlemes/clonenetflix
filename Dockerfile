FROM python:3.11.0

ENV PYTHONUNBUFFERED 1

RUN set -x; \
    apt-get update && \
    apt-get install -y \
    postgresql-client

RUN mkdir -p app/

RUN pip3 install poetry
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY ./pyproject.toml app/

WORKDIR /app

RUN poetry config virtualenvs.create false
RUN poetry install --only main