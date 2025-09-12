#!/usr/bin/env bash
set -o errexit

# Run all migrations
echo "Applying database migrations..."
python manage.py migrate auth --fake-initial
python manage.py migrate --noinput

# Only after migrations are done, create superuser
echo "Creating superuser (if not exists)..."
python manage.py create_user || true

# Optionally seed data
echo "Seeding database..."
python manage.py seed || true

# Start server with Gunicorn
echo "Starting Gunicorn..."

uvicorn portfolio_site.asgi:application --host 0.0.0.0 --port $PORT

