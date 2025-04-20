- 폴더(패키지)를 import 시에 실행됨
- 모듈의 네임스페이스를 유연하게 구성한다

🌈 **초보예시 1**

```python
# models folder

## A.py
class A:
  def __init__(self):
    print("A")

## B.py
class B:
  def __init__(self):
    print("B")

## C.py    
class C:
  def __init__(self):
    print("C")
```

```python
import models.A

model = models.A.A()
```

🌈 **초보예시 2**

```python
# models.py

class A:
  def __init__(self):
    print("A")

class B:
  def __init__(self):
    print("B")
 
class C:
  def __init__(self):
    print("C")
```

```python
import models

model = models.A()
```

- 모든 클래스가 하나의 파일에 들어가야함

🌈 **고수예시**

```python
# models folder

## __init__.py

from .A import A
from .B import B
from .C import C

## A.py
class A:
  def __init__(self):
    print("A")

## B.py
class B:
  def __init__(self):
    print("B")

## C.py    
class C:
  def __init__(self):
    print("C")
```

```python
import models # models가 A,B,C를 갖고 있음

model = models.A()
```

