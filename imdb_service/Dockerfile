# Dockerfile - IMDB-APP
FROM python:3.7-slim
MAINTAINER Satheesh Rathinakumar <satheesh.rl@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends libsasl2-dev python-dev libldap2-dev libssl-dev vim iputils-ping

ENV INSTALL_PATH /imdb_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH
COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install -U requests[security]
COPY . $INSTALL_PATH

RUN echo $INSTALL_PATH
RUN file="$(ls -1 $INSTALL_PATH)" && echo $file

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:imdb_app"]
