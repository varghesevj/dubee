# # Use a lightweight base
# FROM python:3.11-slim

# # Environment setup
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1

# WORKDIR /app

# # Install dependencies first (cached layer)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project files
# COPY . .

# # Collect static files (safe if STATIC_ROOT is set)
# RUN python manage.py collectstatic --noinput || true

# # Expose port (Render auto-sets $PORT but helps locally)
# EXPOSE 8000

# # Run migrations at container startup, not during build
# # CMD python manage.py migrate --noinput && gunicorn dubee.wsgi:application --bind 0.0.0.0:$PORT
# # Create Django superuser automatically
# ENV DJANGO_SUPERUSER_USERNAME=admin
# ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
# ENV DJANGO_SUPERUSER_PASSWORD=admin123

# CMD python manage.py migrate --noinput \
#     && python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true \
#     && gunicorn dubee.wsgi:application --bind 0.0.0.0:$PORT 


# Use a lightweight base
FROM python:3.11-slim

# Environment setup
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Remove collectstatic from build time
# RUN python manage.py collectstatic --noinput || true

# Expose port (Render auto-sets $PORT but helps locally)
EXPOSE 8000

# Django superuser environment variables
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin123

# Run migrations, create superuser, collectstatic, then start gunicorn
CMD python manage.py migrate --noinput \
    && python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true \
    && python manage.py collectstatic --noinput \
    && gunicorn dubee.wsgi:application --bind 0.0.0.0:$PORT
