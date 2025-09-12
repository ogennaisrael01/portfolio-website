#!/usr/bin/env bash
set -euo pipefail

echo "Starting startup script..."

# Wait-for-db + run migrations with retries (useful if DB takes a moment to become available)
RETRIES=12
SLEEP=5

until python manage.py migrate --noinput; do
  RETRIES=$((RETRIES-1))
  echo "Migrate attempt failed. Retries left: $RETRIES"
  if [ "$RETRIES" -le 0 ]; then
    echo "Migrations failed after retries. Exiting."
    exit 1
  fi
  sleep "$SLEEP"
done

echo "Migrations applied successfully."

# Create superuser programmatically (safe, idempotent) using env vars if provided
if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_EMAIL:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  echo "Ensuring superuser ${DJANGO_SUPERUSER_USERNAME} exists..."
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
username='${DJANGO_SUPERUSER_USERNAME}'; email='${DJANGO_SUPERUSER_EMAIL}'; pwd='${DJANGO_SUPERUSER_PASSWORD}'; \
if not User.objects.filter(username=username).exists(): \
    User.objects.create_superuser(username, email, pwd); print('Created superuser'); \
else: print('Superuser already exists')"
else
  echo "Superuser env vars not set; skipping superuser creation."
fi

# Run optional seed (if you have a safe idempotent seed command). '|| true' avoids crash if seed fails.
echo "Running seed (if present)..."
python manage.py seed || echo "Seed command failed or not present; continuing."

# Start the WSGI server (use the correct module name here)
# ✅ IMPORTANT: replace 'portfolio_site' below with your project package name (the folder that contains settings.py & wsgi.py)
uvicorn portfolio_site.asgi:application --host 0.0.0.0 --port $PORT

