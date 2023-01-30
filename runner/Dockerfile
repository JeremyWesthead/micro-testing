FROM python:alpine3.17

RUN  apk update \
  && apk upgrade \
  && apk add ca-certificates \
  && update-ca-certificates \
  && apk add --update coreutils && rm -rf /var/cache/apk/*   \ 
  && apk add --update openjdk11 tzdata curl unzip bash jq\
  && apk add --no-cache nss \
  && rm -rf /var/cache/apk/*

COPY requirements.txt /
RUN pip install -r requirements.txt
ENV PATH /usr/local/lib/python3.11/site-packages:$PATH
RUN echo $PATH

RUN wget -qO- https://github.com/nextflow-io/nextflow/releases/download/v22.10.6/nextflow-22.10.6-all > nextflow
RUN chmod a+x nextflow
ENV PATH /:$PATH
RUN echo $PATH


COPY runner.py /
COPY main.nf /

CMD python3 runner.py