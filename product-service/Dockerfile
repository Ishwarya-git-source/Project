# Use the official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the service files
COPY . .

# Expose the service port
EXPOSE 5003

# Start the service
CMD ["python", "app.py"]
