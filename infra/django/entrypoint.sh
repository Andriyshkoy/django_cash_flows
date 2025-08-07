#!/usr/bin/env bash
set -e

python manage.py collectstatic --noinput
python manage.py migrate --noinput

exec gunicorn \
  config.asgi:application \
  --config /gunicorn.conf.py \
  --worker-tmp-dir /dev/shm