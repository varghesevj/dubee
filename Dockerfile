# Dockerfile
FROM python:3.11-slim

# Environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . /app/

# Collect static files (optional)
RUN python manage.py collectstatic --noinput || true

RUN python manage.py migrate --noinput

# Command to run the app
CMD gunicorn dubee.wsgi:application --bind 0.0.0.0:$PORT
