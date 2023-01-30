FROM python:alpine3.17

COPY requirements.txt /
RUN pip install -r requirements.txt
ENV PATH /usr/local/lib/python3.11/site-packages:$PATH
RUN echo $PATH

COPY queueAPI.py /

CMD uvicorn queueAPI:app --port 8000 --host 0.0.0.0