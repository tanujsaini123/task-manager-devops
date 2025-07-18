FROM python:3.10-slim

WORKDIR /app

COPY backend/app.py .
COPY frontend/static ./static

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
