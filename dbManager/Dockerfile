FROM python:alpine3.17

COPY requirements.txt /
RUN pip install -r requirements.txt
ENV PATH /usr/local/lib/python3.11/site-packages:$PATH
RUN echo $PATH

COPY db.py /

CMD uvicorn db:app --port 8003 --host 0.0.0.0