**Django 정리**



**migrations**

```
python manage.py makemigrations
```

- app > migrations > [number]_initial.py

```
python manage.py migrate
```

- model을 수정하면 db에게 전달함

**super user**

```
python manage.py createsuperuser
```



## ❤️‍🔥 Tip

📌 **cli migration 파일 삭제**

````
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
````

📜**공식문서**

-  [Django-ko](https://docs.djangoproject.com/ko/5.1/)

📌 **migration시에 동기화 오류**

- column 추가시 필수값이 이전 row들에 대한 처리가 필요

**Options**

1. 기존 행들의 컬럼 값이 Null

```python
class Model():
  ...
  new_col = models.Field(null=True)
  ...
```

2. 작업을 중지하고 모델에 Default 값을 지정 

```python
class Model():
  ...
  new_col = models.Field(default=True)
  ...
```

📌 **Foreign key cascading**

```python
foriegn_key = models.ForeignKey("app.Model", on_delete=models.SET_NULL)
```

- fk가 지워져도 null로 남음

```python
foriegn_key = models.ForeignKey("app.Model", blank=True, on_delete=models.SET_NULL)
```

- fk가 지워지면 Row가 사라짐

📌 **Null vs Blank**

- null: 필드에 대한 속성
- blank: null이면서 어드민 패널에서 생성 가능

📌 **Relation**

- **One-to-Many**: ForeignKey
- **Many-to-Many**: ManyToManyField
- **One-to-One**: OneToOneField



## 1. App settings

````
poetry add django
poetry add mysqlclient
poetry add djangorestframework
poetry add pyjwt
poetry add django-environ
poetry add django-cors-headers
````

**config**

```
django-admin startproject config .
```

**gitignore**

```
ctrl+shift+p > add gitignore > python
```

**settings**

```python
SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
]

INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS
```





## 2. User

### 2.1 Default

**create app**

```
python manage.py startapp [app_name]
```

**AbstractUser**

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
```

**Settings**

```
AUTH_USER_MODEL = 'users.Users'
```

**admin**

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
# Register your models here.

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    pass
```



### 2.2 Custom

**model.py**

```python
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    last_login = models.DateTimeField(null=True, blank=True, editable=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
```

**admin**

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import Users


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = ["email", "name", "is_active", "is_superuser", "is_staff"]
    readonly_fields = ["date_joined", "last_login"]  # 수정된 부분

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_superuser", "is_staff")}),
        (
            _("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),  # date_joined 제거
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_superuser",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(Users, UserAdmin)
```



## 3. Common Model

**model.py**

```python
class CommonModel(models.Model):
  """Common Model Definition"""
  created_at = models.DateTimeFiled(auto_now_add=True)
  updated_at = models.DateTimeFiled(auto_now=True)
  
  class Meta:
    abstract = True
```

- abstract가 True일 경우 DB에 저장하지 않음

**other model.py**

```python
class OtherModel(CommonModel):
  """Other Model Definition"""
  ...
```

- common model을 상속받아서 해당 속성이 자동으로 임포트



## 3. Admin Pannel

**Admin defailt vs custom**

1. default

```python
from django.contrib import admin
from [app].models import [Model]

admin.site.register([Model])
```

2. custom

```python
@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
  filedsets = (
    (None, {"fields": ("username", "password")}),
  	(),...
 )
  list_display = [
    "model_colum1",
    "model_colum2",
    "model_colum3",
    ...
  ]
  list_filter = [
    "model_colum1",
    "model_colum1",
    ...
  ]
  search_fileds = [
    "model_colum1",
  ]
  exclude = (
    "model_colum1",
    "model_colum2",    
  )
```

- filedsets: admin page에서 Model의 filed가 보이는 순서를 설정
  - 섹션 안에 filed를 넣어서 제목을 붙일 수 있음
- list_display: admin pannel에 나타낼 컬럼(모델)
- list_filter: admin filter에 나타낼 컬럼(모델)
- search_fileds: admin 검색을 위한 컬럼(모델)
- exclude: 수정할 수 없도록 함



## ⛔️ Trouble Shooting

💥 **Messages**

- django는 SYSTEM_APPS에 이미 message를 가지고 있음
- 신규 application을 message로 가져가면 안됨



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





https://www.hides.kr/938

https://docs.djangoproject.com/en/4.1/topics/auth/customizing/

https://kimdoky.github.io/django/2018/11/26/django-username-verbose/

https://www.hides.kr/942

https://d-life93.tistory.com/424

https://velog.io/@pjh1011409/%EB%A1%9C%EA%B7%B8%EC%9D%B8#-payload



비밀번호암호화: https://velog.io/@misun9283/django-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%95%94%ED%98%B8%ED%99%94-%EB%B0%8F-%ED%86%A0%ED%81%B0-%EB%B0%9C%ED%96%89