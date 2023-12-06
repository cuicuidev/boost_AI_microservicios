FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk add g++

COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps gcc musl-dev

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]