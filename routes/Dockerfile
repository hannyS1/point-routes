FROM python:3.8

RUN apt-get update && apt-get install libffi-dev netcat libgdal-dev postgis -y && apt-get autoremove -y && apt-get clean


RUN mkdir /server

COPY ./requirements.txt /server

RUN pip install -r /server/requirements.txt

COPY . /server

RUN ["chmod", "+x", "/server/run.sh"]

EXPOSE 8000

WORKDIR /server

ENTRYPOINT ./run.sh