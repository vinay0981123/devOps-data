FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/certs
COPY selfsigned.crt /etc/nginx/certs/selfsigned.crt
COPY selfsigned.key /etc/nginx/certs/selfsigned.key

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]