# DRF Starter Template

Django Rest Framework template for my next projects

## Table of Contents

1. [Features](#features)
1. [Setting Postgres](#setting-up-postgres-on-django-project)

### Features

- Custom user model (AbstractUser)
- Social auth (Google)
- Postgres DB
- Multiple settings environment
- Auth endpoints

### Setting Up Postgres on Django Project

To set up PostgreSQL on a Linux system, you will need to do the following steps:

Install the PostgreSQL package:

```bash
sudo apt-get install postgresql postgresql-contrib
```

Start the PostgreSQL service:

```bash
sudo service postgresql start
```

Log in to the PostgreSQL command-line interface as the postgres user:

```bash
sudo -u postgres psql
```

Create a new database and user:

````bash
CREATE DATABASE mydatabase;

CREATE USER myuser WITH PASSWORD 'mypassword';

GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
``

>**Note**: Dont use the username `user` as it will conflict with the command

Exit the PostgreSQL command-line interface:

```bash
\q
````

Update the Django settings to use the new database:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

By following these steps, you should be able to set up PostgreSQL on your Linux system and use it with Django.
