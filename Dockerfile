# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the Django project
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc pkg-config default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn


# Install MariaDB client
RUN apt-get update && apt-get install -y mariadb-client

# Expose the port the app runs on
EXPOSE 8000

# Run the uWSGI server with the specified config
ENTRYPOINT ["sh", "entrypoint.sh"]
