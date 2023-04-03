**Django 정리**

## 0. Tip

- migration 파일 삭제 in shell

````
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
````



## 1. Poetry 설치

````
poetry init
poetry shell
poetry add [add_list]
````

- django, mysqlclient, djangorestframework, pyjwt, django-environ

<br>

## 2. Setting 설정

- config > settings.py

### 2.1 Import

````python
import os
import environ
````

### 2.2 Secret key

.env 파일 생성

````makefile
SECRET_KEY="sc"
PASSWORD="pw"
````

.gitignore에 *env 등록

````python
env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")
````

### 2.3 Application

````python
THIRD_PARTY_APPS = ["rest_framework",
										"rest_framework.authtoken",
										]
CUSTOM_APPS = []
SYSTEM_APPS = ['django.contrib.admin',
							'django.contrib.auth',
							'django.contrib.contenttypes',
							'django.contrib.sessions',
							'django.contrib.messages',
							'django.contrib.staticfiles',
							]
							
INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
````

### 2.4 Time zone

````python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
````

### 2.5 Media

````python
MEDIA_ROOT = "uploads"
MEDIA_URL = "user-uploads/"
````

### 2.6 Database

````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': dbname,
        'USER': 'root',
        'PASSWORD': env("PASSWORD"),
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
````

<br>

## 3. Custom user

### 3.1 Startapp

- poetry shell

````
python manage.py startapp users
````

### 3.2 custom user

- django의 user를 상속받는 custom user 생성
- users > models.py

````python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  pass
````

### 3.3 Setting

- config > settings.py

````python
CUSTOM_APPS = ["users.apps.UsersConfig",]

AUTH_USER_MODEL = 'users.User'
````

### 3.4 Migration

- db.sqlite3 delete
- poetry shell

````
python manage.py makemigrations
python manage.py migrate
````

### 3.5 Custom Fields

- AbstractUser의 field들을 수정함
- users > models.py

````python
class User(AbstractUser):
	# editable=False는 유령 필드로 만들어줌
	first_name = models.CharField(max_length=150, editable=False)
	last_name = models.CharField(max_length=150, editable=False)
````

https://www.hides.kr/938

https://docs.djangoproject.com/en/4.1/topics/auth/customizing/