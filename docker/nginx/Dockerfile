FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/* /etc/nginx/conf.d/

COPY /etc/letsencrypt/live/or24-invenio.cottagelabs.com/fullchain.pem /etc/ssl/certs/or24-invenio.cottagelabs.com.pem
COPY /etc/letsencrypt/live/or24-invenio.cottagelabs.com/privkey.pem /etc/ssl/private/or24-invenio.cottagelabs.com.pem