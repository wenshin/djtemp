#!/bin/sh


tmpPath="/data/log/.tmp/"
if [ ! -x "$tmpPath" ]; then
  mkdir $tmpPath
else
  echo "Directory access permission denied or already exist!"
fi

pidfile=${tmpPath}"{{ project_name }}-master.pid"
if [ -f "$pidfile" ]; then
  uwsgi --stop $pidfile
fi
sleep 1
uwsgi --ini server_conf/uwsgi.ini --deamonize /data/log/{{ project_name }}_uwsgi.log
