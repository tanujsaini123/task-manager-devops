FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install flask flask_sqlalchemy

CMD ["python", "backend/app.py"]
