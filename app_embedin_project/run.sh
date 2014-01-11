sudo /etc/init.d/nginx restart
uwsgi --stop /tmp/{{ project_name }}-master.pid
uwsgi --ini conf/uwsgi.ini --pidfile=/tmp/{{ project_name }}-master.pid
