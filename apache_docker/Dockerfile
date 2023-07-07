FROM ubuntu:latest
RUN apt update && apt install -y apache2 wget unzip
COPY apache2/ports.conf /etc/apache2/
COPY apache2/sites-enabled/blue.conf /etc/apache2/sites-enabled/blue.conf
COPY www  /var/www
CMD ["apache2ctl", "-D", "FOREGROUND"]

