FROM nginx:1.22.1

COPY ./deploy/ /etc/nginx/deploy/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d