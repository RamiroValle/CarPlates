FROM python:3.9

WORKDIR /dbscript

COPY ./requirements.txt /dbscript/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dbscript/requirements.txt

COPY . /dbscript