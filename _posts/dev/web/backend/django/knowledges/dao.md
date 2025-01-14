## DAO

Django에서 **DAO(Data Access Object)** 역할은 일반적으로 **Django의 ORM(Model)**이 수행합니다. Django의 ORM은 데이터베이스와의 상호작용을 추상화하여 객체 지향적으로 데이터를 처리할 수 있게 해줍니다. 이 ORM 시스템이 DAO의 역할을 하며, 이를 확장하거나 커스터마이징할 수도 있습니다.

---

### **DAO(Data Access Object)란?**
- DAO는 데이터베이스와 상호작용하는 객체로, CRUD(Create, Read, Update, Delete) 작업을 캡슐화합니다.
- 데이터베이스 접근 코드를 분리하여 비즈니스 로직과 데이터 접근 로직을 독립적으로 관리할 수 있도록 도와줍니다.
- Django의 모델은 기본적으로 이러한 DAO 역할을 수행합니다.

---

### **Django에서 DAO의 구현 방법**

#### **1. 기본적으로 Django의 모델이 DAO 역할 수행**
Django 모델은 테이블과 객체 간의 매핑을 관리하며, 데이터베이스의 레코드에 접근하고 조작할 수 있는 인터페이스를 제공합니다.

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    # DAO 메서드 추가
    @classmethod
    def create_user(cls, name, email):
        return cls.objects.create(name=name, email=email)

    @classmethod
    def get_user_by_id(cls, user_id):
        return cls.objects.get(id=user_id)

    @classmethod
    def delete_user(cls, user_id):
        return cls.objects.filter(id=user_id).delete()
```

##### **사용 예시**
```python
# 데이터 생성
new_user = User.create_user(name="Alice", email="alice@example.com")

# 데이터 읽기
user = User.get_user_by_id(user_id=1)

# 데이터 삭제
User.delete_user(user_id=1)
```

#### **2. 별도의 DAO 클래스 정의**
프로젝트의 규모가 커지고 데이터 접근 로직이 복잡해질 경우, **별도의 DAO 클래스를 정의**하여 모델과 DAO를 분리하는 방식이 적합합니다.

```python
# dao.py
from .models import User

class UserDAO:
    @staticmethod
    def create_user(name, email):
        return User.objects.create(name=name, email=email)

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def update_user(user_id, **kwargs):
        User.objects.filter(id=user_id).update(**kwargs)

    @staticmethod
    def delete_user(user_id):
        User.objects.filter(id=user_id).delete()
```

##### **사용 예시**
```python
from .dao import UserDAO

# 데이터 생성
new_user = UserDAO.create_user(name="Bob", email="bob@example.com")

# 데이터 읽기
user = UserDAO.get_user_by_id(user_id=1)

# 데이터 업데이트
UserDAO.update_user(user_id=1, name="Robert")

# 데이터 삭제
UserDAO.delete_user(user_id=1)
```

---

### **DAO를 사용하는 이유**

#### **1. 비즈니스 로직과 데이터 접근 로직 분리**
- DAO를 사용하면 데이터베이스 접근 로직이 한 곳에 모이기 때문에 코드의 가독성과 재사용성이 높아집니다.
- 비즈니스 로직에서 데이터 접근 방식을 쉽게 교체하거나 확장할 수 있습니다.

#### **2. 데이터베이스 변경에 대한 유연성**
- 데이터베이스가 변경되거나 ORM에서 SQL로 변경되는 상황에서도 DAO를 통해 데이터 접근 로직을 중앙에서 관리할 수 있습니다.

#### **3. 재사용성 증가**
- 동일한 데이터 접근 로직을 여러 서비스에서 반복적으로 사용할 경우, DAO를 통해 중복 코드를 줄일 수 있습니다.

#### **4. 테스트 용이성**
- DAO는 데이터베이스 접근 로직만 담당하므로, 단위 테스트를 작성하여 데이터베이스 작업을 독립적으로 검증할 수 있습니다.

---

### **Django에서 DAO의 위치**

#### **1. 기본 ORM 사용 (기본 DAO 역할)**
- Django의 ORM(Model)은 기본적으로 DAO 역할을 수행합니다.
- `Model.objects` 메서드를 통해 데이터 접근이 이루어지며, 간단한 CRUD 작업은 추가적인 DAO 클래스 없이 처리 가능합니다.

#### **2. 커스텀 DAO 클래스**
- DAO 클래스는 보통 **`services` 또는 `dao` 디렉토리**에 정의됩니다.
- DAO 클래스는 모델과 독립적으로 존재하며, 특정 테이블 또는 연관된 데이터베이스 작업을 캡슐화합니다.

---

### **DAO와 Service Layer의 관계**
- DAO는 데이터베이스와의 상호작용을 처리하고, 서비스 레이어는 비즈니스 로직을 구현합니다.
- Django 프로젝트에서는 다음과 같은 계층 구조를 가질 수 있습니다:

```
View (Controller) → Service → DAO → Model
```

#### 예시: DAO와 Service 계층 사용
```python
# dao.py
class UserDAO:
    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()
```

```python
# services/user_service.py
from .dao import UserDAO

class UserService:
    @staticmethod
    def find_user_by_email(email):
        return UserDAO.get_user_by_email(email)
```

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.user_service import UserService

class UserView(APIView):
    def get(self, request):
        email = request.GET.get("email")
        user = UserService.find_user_by_email(email)
        if user:
            return Response({"id": user.id, "name": user.name, "email": user.email})
        return Response({"error": "User not found"}, status=404)
```

---

### **결론**
1. Django의 ORM(Model)은 기본적으로 DAO 역할을 수행합니다.
2. 프로젝트가 복잡해지면 데이터 접근 로직을 별도의 **DAO 클래스**로 분리하여 관리할 수 있습니다.
3. DAO는 데이터 접근만을 담당하며, 서비스 계층과 결합하여 비즈니스 로직과 데이터 접근 로직을 분리하는 데 중요한 역할을 합니다.