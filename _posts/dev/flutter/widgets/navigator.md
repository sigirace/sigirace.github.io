### 📍 pushAndRemoveUntil

```dart
Future<T?> pushAndRemoveUntil<T extends Object?>(Route<T> newRoute, bool Function(Route<dynamic>) predicate)
```

- **newRoute**: Route class를 받음 (MaterialPageRoute, ...)
- **predicate**: 쌓여있는 스크린을 지울지 결정
  - `true`면 지우는 것
  - bool을 반환하는 함수가 필요
  - 아래와 같이 사용하는데, 이때 익명함수의 인자로 사용된 route는 flutter가 자동으로 Route 클래스의 인스턴스로 지정함
  - 따라서 이름이 route이던 powercococo 던 상관 없음

```dart
(route) => true
```


