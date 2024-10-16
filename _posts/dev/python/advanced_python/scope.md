## ❤️‍🔥 Scope

- 변수가 어느 스코프에 있는가?
- 변수가 어느 Namespace에 있는가
- Built-in scope > global scope > enclosed scope > local scope
- 각 단계에서 없다면 상위 단계를 찾아봄

📌 **NameSapce**

- Namespace안에 테이블을 생성
- 한쪽에는 이름 그리고 옆에는 연결이 되어있는 객체의 메모리 주소를 저장

🌈 **Example**

```python
x=2023
```

1. 2023이라는 int 객체가 생성됨
2. x라는 변수를 생성함
3. x 변수를 2023 int 객체랑 연결시킴

- namespace

| 이름 | 레퍼런싱된 객체 메모리 주소 |
|--------|--------|
| x | x9odasodqw |

📌 **Function**

- 함수는 함수 자체로 namespace를 가지게 됨

🌈 **Example: novel1이라는 함수 안에 있는 name은 어디에 존재하는가?**

```python
def novel1():
  name = 'Bryan'
  return name
```

1. 선언시 Function class의 인스턴스 객체 주소가 namespace에 등록됨

| 이름  | 레퍼런싱된 객체 메모리 주소 |
| ----- | --------------------------- |
| novel | 9124u81jwq                  |

2. 함수 호출시 function 안에 새로운 namespace가 생성됨

| 이름 | 레퍼런싱된 객체 메모리 주소 |
| ---- | --------------------------- |
| name | 1r912nr3k                   |

3. 함수 실행이 끝나면 새로운 namespace는 지워짐
   - 바깥의 namespace에서 레퍼런싱이 안되기 때문
   - **Q. namespace를 지우는 이유?**
   - **A: 메모리를 save하기 위해**

### 📍 Nested Function

- function 속에 function이 있는 것

### 📍Global

- local 변수로 global 변수를 바꿀 수 없음

```python
name = "kang"

def outer():
  name = name + "_dev"
  print(name)

outer()  
```

```
UnboundLocalError: local variable `name` referenced before assignment.
```

- global 키워드를 사용하여 변경

```python
name = "kang"

def outer():
  global name
  name = name + "_dev"
  print(name)

outer()
print(name)
```

```
kang_dev
kang_dev
```

### 📍Non-local

- local 변수로 enclosed 변수를 바꿀 수 없음

```python
def outer():
  name = "kang"
  print(name)
  
  def inner():
    name = name + "_dev"
    print(name)
  
  inner()
  
outer()
```

```
UnboundLocalError: local variable 'name' referenced before assignment
```

- nonlocal 키워드 사용

```python
def outer():
  name = "kang"
  print("outer", name)
  
  def inner():
    nonlocal name
    name = name + "_dev"
    print("inner", name)
  
  inner()
  print("new outer", name)
  
outer()
```

```
outer kang
inner kang_dev
new outer kang_dev
```



