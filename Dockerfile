FROM python:3.9-slim-bullseye
#FROM python:3.9-alpine
LABEL Maintainer="fgomezdev@gmail.com"

WORKDIR /usr/app/src

COPY requirements.txt check_container.py ./
RUN pip install --no-cache-dir -r requirements.txt

#for debian image
RUN apt-get update

#for alpine image
#RUN apk add --update docker openrc    

#for debian image
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - 
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

ENTRYPOINT ["python", "/usr/app/src/check_container.py"]