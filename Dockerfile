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

# Collect static files (safe if STATIC_ROOT is set)
RUN python manage.py collectstatic --noinput || true

# Expose port (Render auto-sets $PORT but helps locally)
EXPOSE 8000

# Run migrations at container startup, not during build
CMD python manage.py migrate --noinput && gunicorn dubee.wsgi:application --bind 0.0.0.0:$PORT
