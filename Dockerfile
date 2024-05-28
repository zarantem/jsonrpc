FROM python:3.11-alpine

WORKDIR /jsonrpc

COPY . .

RUN pip install -r requirements.txt
