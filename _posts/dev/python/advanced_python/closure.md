## ❤️‍🔥 Closure

📜[추가설명](https://shoark7.github.io/programming/python/closure-in-python)

Python에서 **클로저(closure)**는 함수와 그 함수가 선언된 렉시컬 범위(Lexical Scope)에 있는 변수를 함께 캡처하고 기억하는 개념입니다. 클로저는 일반적으로 함수 안에 다른 함수를 정의하고, 그 내부 함수가 외부 함수의 변수를 참조할 때 형성됩니다. 

### 📍 Lexical Scope

**렉시컬 범위(Lexical Scope)**는 프로그램 코드에서 변수가 정의된 위치에 따라 접근할 수 있는 범위가 결정되는 방식을 의미합니다. Python을 비롯한 대부분의 언어에서는 함수나 블록의 구조에 따라 변수를 찾는 범위가 정해지며, 이런 방식을 **정적 스코핑(Static Scoping)** 또는 **렉시컬 스코핑(Lexical Scoping)**이라고도 합니다.

📌 **렉시컬 범위의 특징**

- **코드 작성 위치**에 따라 변수의 유효 범위가 결정됩니다. 즉, 함수가 호출된 위치와는 관계없이, 함수가 정의된 위치를 기준으로 변수를 찾습니다.
- 함수 내부에서 변수를 참조할 때, 먼저 **자신의 범위**에서 찾고, 그 다음 **외부 범위**에서 찾는 방식으로 올라갑니다.

📌 **클로저의 특징**

1. **중첩 함수**: 클로저를 사용하려면 보통 함수 안에 다른 함수를 정의합니다.
2. **외부 변수 접근**: 내부 함수는 외부 함수의 지역 변수를 사용할 수 있습니다.
3. **상태 유지**: 외부 함수의 실행이 끝나도, 내부 함수는 외부 함수의 변수에 접근할 수 있기 때문에 상태를 유지할 수 있습니다.

🌈 **Example1**

다음은 클로저의 간단한 예제입니다:

```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_closure = outer_function("Hello, Python!")
my_closure()  # "Hello, Python!" 출력
```

위 예제에서 `outer_function`은 문자열 `msg`를 인자로 받고, `inner_function`이라는 내부 함수를 정의하여 반환합니다. 반환된 `inner_function`은 `msg`에 접근할 수 있는 상태를 유지하므로 클로저가 됩니다. 

📌 **클로저의 장점**

1. **데이터 은닉**: 외부 함수의 변수를 숨기고, 내부 함수에서만 접근할 수 있도록 해줍니다.
2. **상태 유지**: 클로저는 상태를 저장하고, 함수를 호출할 때마다 초기화되지 않기 때문에 일종의 데이터 저장 역할을 할 수 있습니다.
3. **재사용성**: 클로저를 사용하여 유연하고 재사용 가능한 함수들을 만들 수 있습니다.

🌈 **Example2**

클로저는 상태를 유지하는 데 유용하여, 예를 들어 카운터 함수를 만들 때 유용하게 사용할 수 있습니다.

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter_a = make_counter()
print(counter_a())  # 1
print(counter_a())  # 2
print(counter_a())  # 3
```

이 예제에서 `make_counter` 함수는 `count`라는 변수를 초기화하고, `counter`라는 내부 함수를 반환합니다. `counter` 함수는 `count` 변수를 증가시키고 반환하는데, `count`는 `make_counter`가 끝나도 사라지지 않고, 내부 함수인 `counter`에서 계속 접근할 수 있어 상태가 유지됩니다.

### 클로저 사용 시 주의사항
- **nonlocal 키워드**: 내부 함수에서 외부 함수의 변수를 수정하려면 `nonlocal` 키워드를 사용해야 합니다.
- **메모리 관리**: 클로저가 외부 변수를 계속 참조하기 때문에 메모리 사용량에 유의해야 합니다. 

이렇게 클로저는 유연하고 상태를 관리할 수 있는 강력한 도구로, 다양한 상황에서 유용하게 사용할 수 있습니다.
