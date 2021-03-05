# Docker file for python simple webservice build

FROM ubuntu:18.04
MAINTAINER Mason889

ENV PYTHON_VERSION=3.8
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -qq && apt -y install --no-install-recommends \
	software-properties-common \
	wget \
	apache2 && \
	rm -rf /var/cache/apk/*
	

# Install get-pip script
RUN wget https://bootstrap.pypa.io/get-pip.py

# Python installation
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -qq && apt install -y --no-install-recommends \
	python${PYTHON_VERSION} \
	python${PYTHON_VERSION}-dev \
	python3-distutils && \
    python${PYTHON_VERSION} get-pip.py && \
	pip install requests && \
    rm -rf /var/cache/apk/*

# Http settings
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

RUN mkdir -p /production/www/cgi-bin
RUN mkdir -p /production/www/lib
COPY cgi-bin /production/www/cgi-bin
COPY lib /production/www/lib
COPY apache2 /etc/apache2
COPY query_page.html /var/www/html/index.html
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/cgi.load

EXPOSE 80

ENTRYPOINT [ "/usr/sbin/apache2" ]
CMD ["-D", "FOREGROUND"]