
# production stage
FROM nginx:stable-alpine as production-stage
COPY  ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY ./dist /usr/share/nginx/html
EXPOSE 5500
CMD ["nginx", "-g", "daemon off;"]