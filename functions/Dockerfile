FROM node:16.13.0-alpine3.13

WORKDIR /serverless/app

RUN npm --loglevel=error install -g serverless && npm --loglevel=error install -g serverless-offline

RUN npm --loglevel=error install -g serverless-python-requirements

COPY . /serverless/app

RUN npm install

RUN apk add py3-pip

RUN pip3 install --no-cache-dir --upgrade -r /serverless/app/requirements.txt

EXPOSE 3000