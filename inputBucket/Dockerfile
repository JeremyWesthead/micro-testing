FROM python:alpine3.17

COPY requirements.txt /
RUN pip install -r requirements.txt
ENV PATH /usr/local/lib/python3.11/site-packages:$PATH
RUN echo $PATH

COPY inputManager.py /
VOLUME /home/jeremy/Documents/Work/testing/microservices/inputBucket/files /files

CMD uvicorn inputManager:app --port 8001 --host 0.0.0.0