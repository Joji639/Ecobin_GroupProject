#!/bin/sh
set -e

if [ "$1" = "celery" ]; then
    shift
    exec celery -A ecobin_backend "$@"
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput 2>/dev/null || true

exec gunicorn ecobin_backend.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers ${WEB_CONCURRENCY:-3} \
    --timeout ${GUNICORN_TIMEOUT:-120}