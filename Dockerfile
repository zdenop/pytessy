FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

#RUN mkdir build

#WORKDIR /build

RUN apt-get update && apt-get install -y python3
RUN apt-get -y install python3-pip

RUN apt-get update && apt-get install -y tesseract-ocr 

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 80

WORKDIR /code/app

CMD python3 -m uvicorn main:app --host 0.0.0.0 --port 80