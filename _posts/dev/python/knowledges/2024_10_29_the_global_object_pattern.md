---
layout: single
title:  'The Global Object Pattern'
toc: true
categories: Python
tags: [Gesign pattern, Python]

---

📜 [참조문서](https://python-patterns.guide/python/module-globals/)
{: .notice}

Python에서 각 모듈은 처음 import될 때 파일의 최상위 레벨에 있는 모든 코드를 실행합니다. 모듈의 최상위 레벨 코드는 `함수`나 `클래스`처럼 호출되지 않아도 import 시 바로 실행되며, 이는 다른 스크립트 언어와도 비슷한 점입니다. 이 방식이 편리하면서도 몇 가지 주의할 사항이 있습니다.

### 1.1 모듈의 최상위 레벨 코드 실행

모듈 최상위에 위치한 코드(=외부 레벨 코드)들은 import 시점에 실행됩니다. 이는 모듈 내에서 설정한 전역 상수, 데이터 구조 등이 사용하는 곳에서 쉽게 접근할 수 있는 장점이 있습니다. 예를 들어, 파일 최상위에 `config`나 `DEFAULT_VALUES`와 같은 상수를 정의해두면 다른 모듈에서 `import`하여 활용할 수 잇습니다.

   ```python
   # config.py 외부 레벨 정의
   API_URL = "https://api.example.com"
   DEFAULT_TIMEOUT = 30
   ```

   ```python
   # main.py 외부 레벨 사용
   from config import API_URL
   ```

### 1.2 **변경 가능한 전역 객체의 위험성**
그러나, 이와 같은 전역 객체가 변경 가능(mutable)한 객체라면 위험할 수 있습니다. 예를 들어, 전역 리스트나 딕셔너리를 사용하는 경우 모듈을 사용하는 다른 코드가 그 객체를 직접 수정할 수 있으며, 의도치 않게 프로그램의 다른 부분에 영향을 미칠 수 있습니다. 이를 방지하려면, 변경 가능 객체는 가급적 함수나 클래스 내부에서 생성하거나, 상수로 사용하려면 튜플과 같은 변경 불가능한(immutable) 자료형으로 선언하는 것이 좋습니다.

   ```python
   # 위험 예시
   # config.py
   SETTINGS = {"timeout": 30}

   # main.py
   from config import SETTINGS
   SETTINGS["timeout"] = 10  # 다른 코드에도 영향을 미침
   ```

### 1.3 **I/O 작업 및 import 시간 비용**
모듈의 최상위 레벨에서 I/O 작업이나 시간이 오래 걸리는 작업을 수행하는 경우, 해당 모듈이 import될 때마다 실행되기 때문에 import하는 데 부하가 생길 수 있습니다. 파일 읽기, 데이터베이스 연결, 네트워크 요청 등은 모듈의 최상위 레벨에서 수행하기보다는 함수로 감싸서 필요할 때 실행되도록 하는 것이 좋습니다.

   ```python
   # 지양할 예시
   # config.py
   with open("settings.json") as f:
       SETTINGS = json.load(f)
   ```

이처럼 전역적으로 데이터를 불러오는 코드를 함수로 작성하여 호출 시점에 실행하도록 만드는 것이 효율적입니다.

   ```python
   # 권장 예시
   # config.py
   def load_settings():
       with open("settings.json") as f:
           return json.load(f)
   ```



## 2. 모듈과 네임스페이스

Python에서 모듈은 각각 독립된 네임스페이스를 갖고 있기 때문에, 서로 다른 모듈에서 같은 이름의 함수나 변수를 정의하더라도 충돌하지 않습니다. 예를 들어, `json` 모듈과 `pickle` 모듈 모두 `loads()`라는 이름의 함수를 가지고 있지만, 서로 다른 기능을 수행하며, 각 모듈 안에서 독립적으로 사용됩니다. 

Python에서 **모든 함수와 클래스가 객체**로 간주되지만, 여기서 말하는 **Module Global 패턴**은 특히 **모듈의 전역 레벨에서 이름이 부여된 일반 객체 인스턴스**를 의미합니다. 즉, 특정 객체를 모듈의 전역 네임스페이스에 두고 다른 코드에서 쉽게 접근할 수 있도록 이름을 할당하는 방식입니다. 이는 코드 구조를 단순하게 하고, 전역 객체를 통해 재사용성을 높이며, 코드 중복을 줄일 수 있습니다.