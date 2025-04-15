# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY temp_app.py .

CMD ["python", "temp_app.py"]