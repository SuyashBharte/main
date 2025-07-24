FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY app /app
COPY app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
