FROM node:16.13.0-alpine3.13

WORKDIR /frontend
COPY ./package.json /frontend/package.json
RUN npm install
COPY . .
EXPOSE 4000