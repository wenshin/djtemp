# Description

1. A nginx+uwsgi+django project template.
2. Virtualenv to manage the dependencies.
3. Different directory tree from official templates.

* Project directory tree is like this:

```
project_name
|
├── .gitignore
├── manage.py
├── project_name_env
├── README.md
├── requirements.txt
├── run.sh
│   
├── project_name
│   ├── apps
│   │   └── __init__.py
│   ├── __init__.py
│   ├── utils
│   │   └── __init__.py
│   ├── settings
│   │   ├── common.py
│   │   ├── dev.py
│   │   ├── __init__.py
│   │   ├── prod.py
│   │   └── test.py
│   ├── static
│   ├── templates
│   │   ├── 404.html
│   │   ├── 500.html
│   │   └── index.html
│   └── utils
│       └── __init__.py
│   
├── server_conf
│   ├── nginx.conf
│   ├── uwsgi.ini
│   └── uwsgi_params
│   
└── static_prod
```

* App directory tree is like:

```
app_name
│   
├── admin.py
├── __init__.py
├── models.py
├── static
│   └── app_name
├── tests.py
└──views.py
```


-------------------
# Usage

## Create a django project which app embeded in apps directory

```
$ django-admin.py startproject --template=/path/to/djtemp/app_embedin_project -e py,sh,ini,conf,txt,md -n .gitignore project_name
```

> Attention: It's need to change "/path/to/" to your own path of djtemp. 
> also change project_name to your own project name.

## Create a django app which staticfiles embeded in

```
$ django-admin.py startapp --template=/path/to/djtemp/static_embedin_app app_name
```

## Install python dependencies
* Need pip installed, skip to next if already installed

```
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```

* Use virtualenv
See http://www.virtualenv.org/en/latest/virtualenv.html.

* Install python dependencies

```
# Move to project directory
$ pip install -r requirements.txt
```

## Develop django
* Run 'cp dev.py.sample dev.py' In settings directory
* Run `python manage.py runserver` to start dev environment
* Static files searching

> Djtemp default support searching static files in every app which installed
> in settings.common.

* Recomment all app codes in apps directory. So in default, djtemp Create a apps.main app to contain the views.index
* Recomment all static, template or custom filters and tags files which belong to a app been put in to it's own folder

## Deploy django

* Install [nginx](http://wiki.nginx.org/Install) and [uwsgi](http://uwsgi-docs.readthedocs.org/en/latest/Install.html)


* Set `settings.common.DEBUG` to `False`
* Move to project directory and run

```
# If you use a database
$ python manage.py syncdb
... # Some settings for database
...
$
$ python manage.py collectstatic
$ sudo sh restart_nginx.sh
$ sudo sh restart_uwsgi.sh
```

* The socket between nginx and uwsgi is using tcp/ip by default.
If you want to use socket file way, you should change it in nginx.conf and uwsgi.ini manually.
Do not forget to active the chomd-socket option in uwsgi.ini

* Default the port is 80 which you can custom in `server_conf/nginx.conf`

### Enable the HTTP Authentication

Uncomment two setttings in server_conf/nginx.conf. Change the path of password file

```
auth_basic "Restricted";
auth_basic_user_file /opt/www/sshow/.htpasswd;
```


## More information see office document
[Django Doc](https://docs.djangoproject.com/en/1.6/)
