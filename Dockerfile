# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only what's needed
COPY backend/ .

# Install Flask
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
