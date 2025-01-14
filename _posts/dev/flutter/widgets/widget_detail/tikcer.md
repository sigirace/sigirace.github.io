📍 **Ticker**

- 각 애니메이션 프레임당 한 번 콜백을 호출함
- ticker를 생성할 때, 함수를 지정할 수 있음
- 지정된 함수는 프레임당 한 번 콜백 호출됨 (초당 60 프레임)

```dart
...
class _ScreenState extends State<ExplicitAnimationsScreen>{
  
  @override
  void initState() {
		super.initState();
    Ticker(
      (elapsed) => print(elapsed),
    ).start();
  }
}
```

- 단 이렇게 얻은 ticker는 화면을 떠나도 계속 실행되며 메로리를 잡아먹음 ☞ `SingleTickerProviderStateMixin` 필요

📍 **SingleTickerProviderStateMixin**

- 현재 트리가 활성화되어 있는 동안만 Ticker를 제공함
- 화면을 떠나면 Ticker를 회수함으로 메모리 관리에 효율적
- 애니메이션 컨트롤러가 하나라 ticker가 하나 필요할 때 사용
- 여러개면 `TickerProviderStateMixin` 사용

📌 **SingleTickerProviderStateMixin을 State에 지정하는 이유**

> `SingleTickerProviderStateMixin`은 `AnimationController`와 같은 애니메이션 객체가 `vsync`를 사용하여 애니메이션을 최적화할 수 있도록 `Ticker`를 제공하는 역할을 합니다. `State` 클래스에 `with` 구문으로 붙는 이유는 `State`가 `Ticker`를 제공해야 하기 때문입니다. `State` 클래스는 위젯의 상태를 관리하고, 애니메이션 컨트롤러는 이 상태에 종속되기 때문에 `State` 클래스에 `SingleTickerProviderStateMixin`을 추가합니다.

📍**vsync**

> `vsync`는 "vertical synchronization"의 약자로, 애니메이션의 프레임이 디스플레이의 새로 고침 주기와 동기화되도록 하는 역할을 합니다. 이를 통해 애니메이션이 부드럽고 효율적으로 실행되며, 불필요한 리소스 낭비를 방지할 수 있습니다.

📍 **elapsed**

`elapsed`는 `Ticker`가 시작된 이후 경과된 시간을 나타내는 `Duration` 객체입니다. `Ticker`는 주기적으로 콜백을 호출하며, 이 콜백의 인자로 `elapsed`를 전달합니다. 이를 통해 애니메이션이나 다른 시간 기반 작업을 수행할 수 있습니다.

📌 **AnimationController에 ticker가 필요한 이유**

- 애니메이션 컨트롤러가 ticker에 연결되기 때문
- 애니메이션 컨트롤러는 가능한 빨리 실행되어야 함 ☞ 부드럽게 애니메이션을 실행하고 싶기 때문

📌 **AnimationController에 ticker를 할당하는 방법**

```dart
class _ScreenState extends State<Screen>
    with SingleTickerProviderStateMixin {
  
  late final AnimationController _animationController = AnimationController(
    vsync: this,
  );

  ...
}
```

- animation controller의 인스턴스화
- this는 현재 클래스로 `SingleTickerProviderStateMixin`가 믹스인 되었기에 `TickerProvider`임

```dart
AnimationController({
  double? value,
  this.duration,
  this.reverseDuration,
  this.debugLabel,
  this.lowerBound = 0.0,
  this.upperBound = 1.0,
  this.animationBehavior = AnimationBehavior.normal,
  required TickerProvider vsync,
}) : assert(upperBound >= lowerBound),
     _direction = _AnimationDirection.forward {
  if (kFlutterMemoryAllocationsEnabled) {
    _maybeDispatchObjectCreation();
  }
  _ticker = vsync.createTicker(_tick); # 이 부분
  _internalSetValue(value ?? lowerBound);
}
```

- 생성자안에 _ticker를 발행하는 부분이 존재

📌 **비동기 초기화**

vsync: this를 사용하는 경우, this는 TickerProvider(즉, SingleTickerProviderStateMixin 또는 TickerProviderStateMixin를 적용한 클래스)를 가리켜야 합니다. 하지만 **비동기 초기화**의 경우, this가 아직 유효하지 않은 상태에서 AnimationController를 초기화하면 오류가 발생합니다.'

**이유: this가 유효하지 않은 경우**

클래스가 아직 완전히 초기화되지 않았거나 Flutter의 생명주기 중 초기화가 완료되기 전에 AnimationController를 생성하려고 하면 오류가 발생합니다. 예를 들어, 클래스 생성자에서 AnimationController를 초기화하려고 하면 vsync로 전달할 this가 준비되지 않은 상태일 수 있습니다.

**해결 방법: initState에서 초기화**

initState는 Flutter의 생명주기에서 **위젯의 상태(State)가 생성된 후 호출**되므로, 이 시점에는 this가 TickerProvider로 완전히 초기화됩니다. 따라서 AnimationController를 안전하게 초기화할 수 있습니다.

📌 **Mixsin 비유**

- SingleTickerProviderStateMixin을 믹스인으로 추가하는 것은 클래스에 “추가 장비를 장착”하는 것과 같습니다.
- 하지만 이 장비가 완전히 작동하려면 **클래스가 완성된 후**(즉, initState 이후)여야 합니다.
- 따라서, AnimationController를 초기화할 때, “장비가 작동 중”인 시점(즉, initState)에서 설정해야 문제가 없습니다.