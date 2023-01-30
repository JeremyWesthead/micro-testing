FROM python:alpine3.17

COPY requirements.txt /
RUN pip install -r requirements.txt
ENV PATH /usr/local/lib/python3.11/site-packages:$PATH
RUN echo $PATH

COPY outputManager.py /
VOLUME /home/jeremy/Documents/Work/testing/microservices/outputBucket/files /files
CMD uvicorn outputManager:app --port 8002 --host 0.0.0.0