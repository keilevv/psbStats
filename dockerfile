FROM python:3.6-buster 
RUN pip3 install flask
RUN pip3 install mpu
RUN pip3 install numpy
RUN pip3 install requests

COPY . /stats
WORKDIR /stats

ENV FLASK_APP=stats.py

ENV FLASK_ENV=development
CMD flask run --host=0.0.0.0


