# Start from a minimal Python image
FROM python:3.10‑slim

# Set working dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY backend/ backend/
COPY templates/ templates/
COPY static/ static/

# Expose the port
EXPOSE 5000

# Run with Gunicorn (3 workers)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "backend.app:app"]
