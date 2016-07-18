FROM debian:jessie
MAINTAINER jsongo<jsongo@qq.com>

ENV CONSUL_VERSION=0.6.4
ENV DOCKER_BASE_VERSION=0.0.4

RUN apt-get update
RUN apt-get install -y curl wget

RUN wget https://releases.hashicorp.com/docker-base/${DOCKER_BASE_VERSION}/docker-base_${DOCKER_BASE_VERSION}_linux_amd64.zip && \
    unzip -d /bin consul_${CONSUL_VERSION}_linux_amd64.zip

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash", "-c"]
