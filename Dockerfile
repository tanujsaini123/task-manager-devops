# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy only the backend app.py to the container
COPY backend/app.py .

# Install Flask
RUN pip install flask

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
