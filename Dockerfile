FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev netcat-openbsd && rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

COPY wait_for_db.sh /app/wait_for_db.sh
RUN chmod +x /app/wait_for_db.sh

CMD ["./wait_for_db.sh"]
