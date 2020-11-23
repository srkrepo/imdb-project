# Base image
FROM nginx:1.15.9-alpine

# Nginx will listen on this port
EXPOSE 80

# Remove the default config file that
RUN rm /etc/nginx/conf.d/default.conf

# We copy the requirements file in order to install
COPY /prod.conf /etc/nginx/conf.d

# We copy the html file in order to view
COPY /index.html /usr/share/nginx/html
