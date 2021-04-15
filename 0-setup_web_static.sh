#!/usr/bin/env bash
# script that sets up your web servers for
# the deployment of web_static.

# Install Nginx or Update dependencies
if [[ ! -e /etc/nginx/sites-available/default ]]; then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install nginx
fi

# Create folders /data/web_static/releases/test
if [[ ! -e /data/web_static/releases/test ]]; then
    mkdir -p /data/web_static/releases/test
fi
if [[ ! -e /data/web_static/shared ]]; then
    mkdir -p /data/web_static/shared
fi

# Create index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# deleted simbolic link
if [[ -e /data/web_static/current ]]; then
    rm /data/web_static/current
fi

# Create simbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

# owner ubuntu
chown -R ubuntu:ubuntu /data

# Add /hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# start service
sudo service nginx start
