FROM ubuntu:focal

RUN apt-get update
RUN apt-get -y install software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get -y install libgl1-mesa-glx python3.11 python3-pip
RUN apt-get -y install python3.11-distutils

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .
