FROM python:3.8.5

WORKDIR /usr/src/app/web

RUN pip install poetry==1.0.9
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY ./ ./
