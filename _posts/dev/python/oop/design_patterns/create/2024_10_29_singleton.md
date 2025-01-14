---
layout: single
title:  '[생성#1] Singleton'
toc: true
categories: Python
tags: [Singleton pattern, Python]


---

📜 [참조문서](https://python-patterns.guide/gang-of-four/singleton/)
{: .notice}

## 💬 싱글톤을 왜 쓸까..?

### 1. 싱글톤 정의

- 인스턴스가 오직 1개만 생성됨
- 즉, 하나의 인스턴스를 생성해 사용하는 디자인 패턴

### 2. 적용 상황

- 레지스트리 같은 설정 파일의 경우 여러 객체가 생성된다면 설정 값이 변경될 위험이 있음 -> 한 곳에서 제어하기 위함
- 같은 요청이 여러번 생성되는 경우 매번 인스턴스가 생긴다면 메모리가 낭비됨

✏️ **목적**

```
인스턴스를 오직 1개만 만들어야 함(한 곳에서만 제어할 수 있도록)
만든 인스턴스에 글로벌하게 접근하는 방식을 제공해야 함
```

### 3. 사용 방법

- 앱 시작시 (Eager initialization)
- 객체 호출시 (Lazu initialization)

### 4. 사용방법 구체

**1. private 생성자에 static 메소드**

- 객체를 호출할 때 인스턴스를 생성하는 Lazy initialization 방식
- 가장 간단하고 보편적인 방식
- 많은 스레드가 동시에 생성 체크 문에 접근 시 모두 객체를 반환하게 됨 -> 멀티스레드 환경에서 안전하지 않음

📌 **왜 안전하지 않은가?**

Django, FastAPI, Flask 등의 백엔드에서 멀티스레드 환경을 구성하였을 때, 각 스레드들이 하나의 인스턴스에 동시에 접근할 수 있다. 물론 Python은 GIL을 통해서 CPU Bounded 작업의 바이트코드 실행을 단일 스레드로 제한한다. 하지만 GIL이 있다고 해서 멀티스레드 환경에서 동시에 인스턴스를 생성하는 시도가 완전히 차단되지는 않는다. 그 이유는 객체가 이미 생성되었는지 확인하고 객체를 생성하는 작업이 단일 python 명령어가 아니기 때문이다. 즉, 이 작업들은 여러 바이트코드 명령어로 구성되며 GIL은 이러한 바이트코드가 수행되는 동안 스레드를 교체할 수 있다. 

🌈 **구현**

```python
class SingletonClass:
    _instance = None  # Static 변수로 인스턴스를 보관
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initializing instance")
```

**2. 동기화를 사용해 멀티쓰레딩 안전성 보장**

- Thread lock을 통해 Thread Safe하게 만듦

🌈 **구현**

```python
import threading

class SettingsSynchronized:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:  # 동기화 블록
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance
```

### 4. 단점

- 인스턴스 간에 결합도가 높아짐
  - 싱글톤 클래스 수정이 일어날 경우 많은 곳에서 영향이 생길 수 있음
  - 개방-폐쇄 원칙을 위배
- 상속을 할 수 없어(생성을 못하니) 단위 테스트가 불가능

<br>

## ✏️ Singleton in Python

Python에서는 일반적인 인스턴스 생성 문법을 그대로 사용할 수 있도록 하면서, Singleton 인스턴스를 반환하는 `__new__()` 메서드를 재정의할 수 있습니다. 더 나아가 Pythonic한 접근법으로는 Singleton 객체를 전역적으로 접근할 수 있도록 하는 "Global Object Pattern"을 사용하는 방법이 있습니다. 

### 1. Python에서의 Singleton 패턴 구현: `__new__()` 메서드 사용
Python은 다른 언어보다 더 유연하게 Singleton 패턴을 구현할 수 있습니다. `__new__()` 메서드를 활용하여 기존 생성자 문법(`Singleton()`)을 사용할 수 있도록 하면서도, 한 번 생성된 인스턴스를 반환하게 할 수 있습니다. Python에서 이 방법은 매우 일반적이고, Pythonic한 방식으로 여겨집니다. 아래 예시를 보겠습니다:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

이렇게 하면 `Singleton()`을 호출할 때마다 항상 같은 인스턴스를 반환합니다. 기존 `get_instance()` 메서드 대신 `Singleton()`을 호출하는 것만으로도 Singleton 패턴을 만족시키며, 사용법이 더 자연스럽고 직관적입니다. 또한, Python에서 `__new__()`는 인스턴스 생성 전 초기화 작업을 담당하므로, 이 방법을 사용하면 Python의 메모리 구조와 객체 초기화 관습에 맞춘 구현이 됩니다.

### 2. 더 Pythonic한 접근법: Global Object Pattern
전역적으로 접근 가능한 단일 객체를 생성해야 할 때, 더 Pythonic한 방식으로 "Global Object Pattern"을 사용할 수 있습니다. 이 패턴은 클래스의 제한 없이 전역 변수를 통해 객체에 접근하는 방식입니다. 단순히 모듈 레벨에서 객체를 선언하여 이를 전역적으로 사용할 수 있게 하고, 필요 시 모듈 자체를 싱글톤 객체로 활용할 수도 있습니다.

다음은 Global Object Pattern을 이용한 예시입니다:

```python
# my_singleton.py 모듈
class MySingleton:
    def __init__(self):
        self.value = "Singleton Instance"

singleton_instance = MySingleton()
```

그리고 다른 모듈에서 `singleton_instance`를 가져와 사용할 수 있습니다:

```python
# another_module.py
from my_singleton import singleton_instance

print(singleton_instance.value)  # Singleton Instance
```

이 접근법은 Singleton 패턴을 구현하지 않고도 단일 객체에 접근할 수 있게 하며, 코드가 더 간결해지고 이해하기 쉬워집니다. Python에서는 모듈 자체가 싱글톤처럼 작동할 수 있기 때문에 객체를 전역적으로 관리할 필요가 있을 때 Pythonic하게 모듈 변수를 활용하는 방법입니다.

