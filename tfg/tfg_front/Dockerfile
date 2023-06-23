# App environment -> Prepare the vue.js build
FROM node:18.12.1-alpine as build-stage
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm i
COPY . .
RUN npm run build

# Server environment -> Deploying NGINX build
FROM nginx as production-stage

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

# Clean html and conf folders and copy the vue-build files
RUN rm -rf /usr/share/nginx/html/*
RUN rm -rf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /app/nginx/nginx.conf /etc/nginx/conf.d/
COPY --from=build-stage /app/dist /usr/share/nginx/html
