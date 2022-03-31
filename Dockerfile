FROM python:latest

LABEL Maintainer="fgomezdev@gmail.com"

WORKDIR /usr/app/src

RUN apt-get update
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY check_container.py ./

ENTRYPOINT ["python", "/usr/app/src/check_container.py"]