# DJANGO REST API

Rest API made using Django, Django-Rest-Framework and MySQLite


# Main Features

> Register, Update, Verify Users

> Generate Token for registered users, and genereate a token based email verification link

> Create, Retreive, Update, Delete Events

**Tech Used**

- Django
- Django Rest Framework
- Django Rest Framework simplejwt
- Pillow


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements and virtualenv to create Virtual Environment.

> install the dependencies first
```bash
pip install -r requirements.txt
```
>Start MySQL Server and Create MySQL Database
```bash
CREATE DATABASE database_name CHARACTER SET utf8;
```

>Add MySQL database credentials in project/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER':'database_user',
        'PASSWORD':'database_password',
        'HOST':'localhost',
        'PORT':''
    }
}
```


## Usage

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Endpoints

>Registering User

- http://127.0.0.1:8000/api/user/create/

>Generating Token

- http://127.0.0.1:8000/api/user/token/

>Events


- GET       http://127.0.0.1:8000/api/user/token/
- POST      http://127.0.0.1:8000/api/user/token/
- GET       http://127.0.0.1:8000/api/user/token/:id/
- PUT       http://127.0.0.1:8000/api/user/token/:id/
- DELETE    http://127.0.0.1:8000/api/user/token/:id/