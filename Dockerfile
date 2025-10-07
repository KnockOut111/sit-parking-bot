# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg ca-certificates xvfb chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Confirm installations
RUN chromium --version && chromedriver --version

# Setup working directory
WORKDIR /app
COPY app/ /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot headlessly
CMD ["python", "main.py"]
