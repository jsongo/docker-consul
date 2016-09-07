FROM debian:jessie
MAINTAINER jsongo<jsongo@qq.com>

ENV CONSUL_VERSION=0.6.4
ENV DOCKER_BASE_VERSION=0.0.4

RUN apt-get update
RUN apt-get install -y wget unzip

RUN wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    unzip consul_${CONSUL_VERSION}_linux_amd64.zip

RUN apt-get install -y curl
RUN apt-get install -y python 
RUN apt-get install -y python-pip \
    pip install supervisor \
    echo_supervisord_conf > /etc/supervisord.conf \
    echo "[include]" >> supervisord.conf && \
    echo "files = /etc/supervisord.d/*.ini" >> supervisord.conf

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash", "-c"]
