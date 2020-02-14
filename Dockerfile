FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        wget \
        git \
	pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        python3-wheel \
        python3-numpy \
        openjdk-8-jdk \
        gnupg2 \
	libboost-all-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
	bash-completion \
	unzip

COPY ./ /edgecomputing

WORKDIR /edgecomputing

RUN pip3 install -U pip 
RUN pip3 install -r requirements.txt


EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]

