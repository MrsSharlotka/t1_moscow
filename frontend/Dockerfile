#STAGE 1
FROM node:20.11-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

#STAGE 2
FROM caddy:2-alpine AS serve
COPY --from=build /usr/src/app/dist /srv
