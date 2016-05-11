FROM python:3.5

COPY requirements.txt /projects/

RUN pip install -r /projects/requirements.txt
