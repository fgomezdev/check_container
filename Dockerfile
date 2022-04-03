FROM python:3.9-alpine
LABEL Maintainer="fgomezdev@gmail.com"

WORKDIR /usr/app/src

COPY requirements.txt check_container.py ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/usr/app/src/check_container.py"]