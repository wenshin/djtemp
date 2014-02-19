#!/bin/sh


tmpPath="{{ project_directory }}/.tmp/"
if [ ! -x "$tmpPath" ]; then
  mkdir $tmpPath
else
  echo "Directory access permission denied or already exist!"
fi


# Nginx scripts
sudo ln -f -s {{ project_directory }}/server_conf/nginx.conf /etc/nginx/sites-enabled/{{ project_name }}_nginx.conf

sudo /etc/init.d/nginx restart


# Uwsgi scripts
pidfile=${tmpPath}"{{ project_name }}-master.pid"
if [ -f "$pidfile" ]; then
  uwsgi --stop $pidfile
fi
  uwsgi --ini server_conf/uwsgi.ini
