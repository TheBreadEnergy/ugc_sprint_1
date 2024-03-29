FROM python:3.12

WORKDIR /opt/app


ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_ROOT_USER_ACTION=ignore \
  DOCKERIZE_VERSION="v0.7.0" \
  PYTHONDONTWRITEBYTECODE=1



RUN groupadd -r flask && useradd -d /opt/app -r -g flask flask \
    && chown flask:flask -R /opt/app/

COPY requirements.txt requirements.txt

COPY docker-entrypoint.sh docker-entrypoint.sh

RUN apt-get update  \
    && apt-get -y install netcat-traditional \
    curl \
    git  \
    wget \
    && wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xzf - -C /usr/local/bin \
    && apt-get autoremove -yqq --purge wget && rm -rf /var/lib/apt/lists/*  \
    && python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .


RUN chmod +x docker-entrypoint.sh

EXPOSE 5001

USER flask

ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]

