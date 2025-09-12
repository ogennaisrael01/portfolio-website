#!/usr/bin/env bash
#!/usr/bin/env bash
set -o errexit

# Run migrations again just to be safe
python manage.py migrate --noinput

# Create superuser (if not exists) and seed
python manage.py create_user || true
python manage.py seed || true

# Start server

uvicorn portfolio_site.asgi:application --host 0.0.0.0 --port $PORT

