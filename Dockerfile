FROM python:3.8-slim-buster as requirements

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade poetry
RUN poetry config virtualenvs.create false

WORKDIR /cognite

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

FROM python:3.10-slim-buster
RUN apt-get update & apt-get upgrade
RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python
RUN mkdir /usr/src/app && chown python:python /usr/src/app
WORKDIR /usr/src/app
COPY --chown=python:python pyproject.toml .
COPY --chown=python:python mqtt_extractor ./mqtt_extractor
COPY --chown=python:python tests ./tests
ADD pyproject.toml ./pyproject.toml

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install



ENTRYPOINT [  "poetry", "run", "main", "config/config.yaml" ]
#ENTRYPOINT [ "poetry", "run", "test_kchief", "config/config.yaml" ]
