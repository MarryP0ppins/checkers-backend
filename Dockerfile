FROM node:14 as setup
RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build
