
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/scr/app

RUN apk update && apk add postgresql-dev \
			  gcc \
			  python3-dev \
			  musl-dev

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
