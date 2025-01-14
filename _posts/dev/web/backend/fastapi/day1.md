## Setting

```
poetry add fastapi
poetry add "uvicorn[standard]"
poetry add py-ulid
poetry add "passlib[bcrypt]"
poetry add bcrypt==3.2.2
poetry add sqlalchemy mysqlclient alembic

brew install mysql pkg-config # 만약 macOS 환경에서 mysql이 설치되어 있지 않은 경우
```

- fastapi를 구동시키려면 ASGI 서버가 필요함
- 공식문서에서는 유비콘 추천



```
docker run --name mysql-local -p 3306:3306/tcp -e MYSQL_ROOT_PASSWORD=test -d mysql:8
```

- user: root
- password: test



## 클린 아키텍처가 강조하는 것

- 관심사 분리와 계층형 아키텍처: 소프트웨어의 구성 요소들을 관심사에 따라 분리 -> 4개의 계층으로 나뉘어짐
- 인터페이스 우선: 구성 요소들의 인터페이스를 먼저 정의해 사용하며 세부 구현은 필요한 시점에 함
- 의존성 규칙: 핵심 원칙으로 소스코드 의존성은 항상 외부에서 내부로 향해야 하며 가장 중요한 코드(비즈니스 규칙)는 시스템의 중심에 있어야 함



## 클린 아키텍처의 주요 4계층

- 소프트웨어를 여러 개의 계층으로 나누고 각 계층에 있는 구성 요소는 안쪽 원에 있는 구성 요소에만 의존성을 가지도록 함
- 안쪽 원에 존재하는 구성 요소는 바깥쪽에 독립적
- 안쪽으로 들어갈수록 고수준의 구성 요소
  - 고수준: 추상화된 관점에서 문제를 해결하는 개념적 관점
  - 저수준: 구체적이거나 세부적인 관점을 나타냄
- `엔티티:도메인`
- `유스케이스:어플리케이션`
- `인터페이스 어댑터:인터페이스`
- `프레임워크 및 드라이버:인프라`



**1. 도메인**

- `도메인`: 애플리케이션이 해결하고자 하는 특정한 주제나 분야
- `도메인 모델`: 도메인의 핵심 개념, 엔티티, 도메인 간의 관계, 도메인이 지켜야 하는 규칙 및 도메인의 상태
- `저장소`: 외부 시스템인 데이터베이스에 저장하는 데이터 저장소를 기술하는 모듈
- `도메인 계층`: SW 내에서 핵심 비즈니스 로직과 엔터프라이즈의 핵심 도메인 관련 기능을 관리하고 구현하는 부분
- `엔티티`: 비즈니스 도메인에서의 실제 개념이나 객체를 표현
  - 예) 은행 애플리케이션의 엔티티는 계좌, 거래, 고객 등
  - 도메인 계층은 독립적으로 존재하며 비즈니스 도메인 그 자체에 집중함
  - 도메인 계층이 데이터베이스 스키마, 사용자 인터페이스 또는 외부 시스템에 대한 의존성을 갖지 않아야 함



[user]

- domain: 해결하고자 하는 특정 문제 영역이나 분야, User Domain은 "회원"이 도메인
  - repository : 저장소, 데이터를 저장하거나 불러오는 방법 정의
    - user_repo.py : user 데이터를 저장하거나 불러오는 방법 정의
      - (Interface) IUserRepository : 데이터를 저장(영속화)하기 위한 인터페이스, 구현체는 인프라 계층에 존재
        - save
        - find_by_email
  - user.py : 도메인 모델, 데이터의 구조와 형식 정의
    - (class) Profile : VO - 식별자를 가지지 않음
    - (class) User : 도메인 | 엔티티 - 식별자를 가짐
- application
  - user_service.py [유즈케이스]
    - (class) UserService : 회원과 관련한 여러 유즈케이스 집합
      - (function) create_user : 회원 가입을 하는 케이스
- interface
  - controllers
    - user_controller.py
      - router : 외부 시스템과의 통신 담당
      - CreateUserBody, CreateUserResponse : 외부와 내부의 데이터를 각각에 맞게 변환
      - get_user_service : 외부 요청과 서비스 매핑
      - create_user (post) : 외부 요청을 서비스를 사용해 수행
- infra
  - db_models : DB ORM
    - user.py 
      - User
  - repositroy
    - user_repo.py : 도메인 부분 영속화 실제 구현 코드
      - UserRepository (IUserRepository)
        - save
        - find_by_email



### Alembic ORM

**database.py**

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:test@127.0.0.1/fastapi-ca"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
```

- `SessionLocal` 클래스는 데이터 베이스 세션과 관련되어 있음
- 이 클래스의 객체가 생성되면 데이터 베이스 세션이 생성됨
- 이때 옵션으로 autocommit을 false로 할 경우 별도의 커밋 명려잉 없으면 커밋이 자동으로 수행되지 않음
- true일 경우 롤백 불가능

```
alembic init migrations
```

**alembic.ini**

```
file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

sqlalchemy.url = mysql+mysqldb://root:test@127.0.0.1/fastapi-ca
```

**database_models.py**

```python
import user.infra.db_models.user
```

**migrations.env.py**

```
import database
import database_models

target_metadata = database.Base.metadata,
```

- migration/version 디렉토리에 파일이 생성됨

```
alembic revision --autogenerate -m "add User Table"
```

- migration 수행됨

```
alembic upgrade head
```

- migrate 수행됨

```
alembic downgrade -1 
```

- head 만큼 rollback

