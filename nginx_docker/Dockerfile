FROM nginx:1.25.1
COPY ./nginx_docker/nginx.conf /etc/nginx.conf
COPY ./nginx_docker/00-jsonlog.conf /etc/nginx/conf.d/
RUN rm -f /etc/nginx/conf.d/default.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

