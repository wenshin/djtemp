# Description

1. A nginx+uwsgi+django project.
2. Virtualenv to manage the dependencies.
3. Different directory tree from official templates.

* Project directory tree is like this:

```
project_name
|
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
.
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
$ django-admin.py startproject --template=/path/to/django_templates/app_embedin_project -e py,sh,ini,conf,txt,md -n .gitignore project_name
```

## Create a django app which staticfiles embeded in

```
$ django-admin.py startapp --template=/path/to/django_templates/static_embedin_app app_name
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
# /path/to/project_name/
$ pip install -r requirements.txt
```

## Develop django
* Set `settins.common.DEBUG` to `True`
* Run `python manage.py runserver` to start dev environment
* Static files searching

> Djtemp default support searching static files in every app which installed
> in settings.common.

* Recomment all app codes in apps directory. So in default, djtemp Create a apps.main app to contain the views.index
* Recomment all static, template or custom filters and tags files which belong to a app been put in to it's own folder

## Deploy django
* Set `settings.common.DEBUG` to `False`
* Move to project directory and run

```
$ python manage.py syncdb
... # Some settings for database
...
$
$ python manage.py collectstatic
$ sudo sh run.sh
```

* Default the port is 80 which you can custom in `server_conf.nginx.conf`

## More information see office document
[Django Doc](https://docs.djangoproject.com/en/1.6/)
