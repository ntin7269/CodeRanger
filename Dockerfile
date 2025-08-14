FROM python:3.11

# Install g++
RUN apt-get update && apt-get install -y g++

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=OJ.settings
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Run migrations and start Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver --insecure 0.0.0.0:8000"]

