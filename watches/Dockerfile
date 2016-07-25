FROM debian:jessie
MAINTAINER jsongo<jsongo@qq.com>

ENV CONSUL_VERSION=0.6.4
ENV DOCKER_BASE_VERSION=0.0.4

RUN apt-get update
RUN apt-get install -y wget unzip

RUN wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    unzip consul_${CONSUL_VERSION}_linux_amd64.zip

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash", "-c"]
