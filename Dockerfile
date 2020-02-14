FROM ubuntu:18.04

RUN apt-get update

COPY ./ /edgecomputing

WORKDIR /edgecomputing
