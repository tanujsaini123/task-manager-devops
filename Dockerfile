FROM python:3.10-slim

WORKDIR /app

COPY backend/app.py .
COPY frontend ./frontend

RUN pip install flask

CMD ["python", "app.py"]
