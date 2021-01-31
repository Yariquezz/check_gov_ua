# pull official base image
FROM nginx:1.19.0-alpine

# copy nginx configurations
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d