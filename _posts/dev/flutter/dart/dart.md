**📍 cascade operator**

> `..` 연산자는 Dart에서 **cascade operator**라고 불립니다. 이 연산자를 사용하면 동일한 객체에 대해 여러 메서드 호출이나 속성 설정을 연속적으로 수행할 수 있습니다. 

```dart
_animationController = AnimationController(
  duration: const Duration(seconds: 10),
  vsync: this,
)..addListener((){});
```

```dart
_animationController = AnimationController(
  duration: const Duration(seconds: 10),
  vsync: this,
);
_animationController.addListener((){});
```

- 위 두 코드는 동일하게 작용

**📍final**

- dart가 변화가 없는 변수에는 자동으로 final을 붙임

