FROM python:3.11-slim

WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app-auth.py .
COPY login.html .
COPY admin-dashboard.html .
COPY rally-sync.html .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app-auth.py"]
