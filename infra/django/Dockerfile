FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-deps --wheel-dir /wheels -r requirements.txt

FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y build-essential libpq5 libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache --no-index --find-links /wheels /wheels/*

COPY ./../../ .
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# gunicorn cfg
COPY gunicorn.conf.py /gunicorn.conf.py

# healthcheck: запрашиваем /health/ в контейнере
HEALTHCHECK CMD curl -f http://localhost:8000/health/ || exit 1

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
