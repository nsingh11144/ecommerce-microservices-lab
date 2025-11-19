# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (for efficient caching)
COPY requirements.txt .

# Install dependencies (no cache for smaller image)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Flask default port
EXPOSE 5000

# Set environment variable so Flask runs in production mode
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the app
CMD ["flask", "run"]
