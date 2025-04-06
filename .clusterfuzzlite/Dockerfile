FROM gcr.io/oss-fuzz-base/base-builder-python:v1@sha256:200f2f19db18657dd21e4954838500603c510d520fb567a3e7601d2a42ab2930

RUN apt-get update && apt-get install -y make autoconf automake libtool

COPY . $SRC/cronk
WORKDIR cronk
COPY .clusterfuzzlite/build.sh .clusterfuzzlite/*.dict $SRC/

RUN pip3 install git+https://github.com/HypothesisWorks/hypothesis.git@705bb26c0dead01ce119dab37e977b7aedb26d1c
