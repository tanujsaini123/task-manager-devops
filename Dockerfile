FROM python:3.10-slim

WORKDIR /app

COPY backend/app.py .
COPY backend/static ./static

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
