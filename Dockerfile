FROM python:3.11-slim
#RUN apt update -y && apt-get install -y build-essential

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt
#RUN apt-get update -y
#RUN apt-get upgrade -y
#RUN apt-get install -y python3-pip python-dev build-essential
#RUN apt-get install python -y
RUN pip install -r requirements.txt

COPY . .