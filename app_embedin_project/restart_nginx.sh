#!/bin/sh

# Nginx scripts
sudo ln -f -s {{ project_directory }}/server_conf/nginx.conf /etc/nginx/sites-enabled/{{ project_name }}_nginx.conf

sudo /etc/init.d/nginx restart
