# Base image with Python
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /todo_application

# Install dependencies for psycopg2
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies in todo_application
COPY requirements.txt .
# No-cache-dir is used to avoid caching the package index
RUN pip install --no-cache-dir -r requirements.txt

# Copy wait-for-it.sh script and make it executable
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copy the Django app code
COPY . .

# Specify the Django directory if manage.py is in a subfolder like `todo_project`
WORKDIR /todo_application/todo_project

# Run database migrations and collect static files before starting Gunicorn server
# This section will ensure the database is prepared and static files are in place

# Start the Gunicorn server
CMD ["gunicorn", "todo_project.wsgi:application", "--bind", "0.0.0.0:8000"]
