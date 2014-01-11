# Description

1. A nginx+uwsgi+django project.
2. Virtualenv to manage the dependencies.
3. Different directory tree from official templates.

* Project directory tree is like this:

```
.
├── manage.py
├── project_name
│   ├── apps
│   │   └── __init__.py
│   ├── __init__.py
│   ├── libs
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
│   │   ├── base.html
│   │   └── index.html
│   └── utils
│       └── __init__.py
├── project_name_env
├── README.md
├── requirements.txt
├── run.sh
├── server_conf
│   ├── nginx.conf
│   ├── uwsgi.ini
│   └── uwsgi_params
└── static_prod
```

* App directory tree is like:

```
.
├── admin.py
├── admin.pyc
├── __init__.py
├── __init__.pyc
├── models.py
├── models.pyc
├── static
│   └── app_name
├── tests.py
├── tests.pyc
├── views.py
└── views.pyc
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
