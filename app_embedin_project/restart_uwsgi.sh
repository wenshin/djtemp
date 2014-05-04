#!/bin/sh


tmpPath="{{ project_directory }}/.tmp/"
if [ ! -x "$tmpPath" ]; then
  mkdir $tmpPath
else
  echo "Directory access permission denied or already exist!"
fi

pidfile=${tmpPath}"{{ project_name }}-master.pid"
if [ -f "$pidfile" ]; then
  uwsgi --stop $pidfile
fi
  uwsgi --ini server_conf/uwsgi.ini
