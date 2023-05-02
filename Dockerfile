FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY r.txt /app/r.txt
COPY . /app
RUN pip install -r r.txt
RUN apt-get update && apt-get install -y iputils-ping curl net-tools
