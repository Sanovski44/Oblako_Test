FROM joyzoursky/python-chromedriver:3.7-selenium


RUN apt-get -y update
RUN apt-get install -y python3-pip

RUN pip3 install behave selenium behave-html-formatter

ENV docker true

WORKDIR /app
COPY . .