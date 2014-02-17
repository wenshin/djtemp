#!/bin/sh

# Nginx scripts
sudo ln -f -s {{ project_directory }}/server_conf/nginx.conf /etc/nginx/sites-enabled/{{ project_name }}_nginx.conf
sudo /etc/init.d/nginx restart

# Uwsgi scripts
pidfile="/tmp/{{ project_name }}-master.pid"
if [ -f "$pidfile" ]; then
  uwsgi --stop /tmp/{{ project_name }}-master.pid
fi
  uwsgi --ini server_conf/uwsgi.ini
