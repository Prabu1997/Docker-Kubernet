FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    iputils-ping \
    dnsutils \
    traceroute \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your script into the container
COPY diagnose.py .

# Set default command
CMD ["python3", "diagnose.py"]