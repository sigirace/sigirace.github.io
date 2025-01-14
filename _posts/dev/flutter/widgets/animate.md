### 📍 AnimatedCrossFade

- `firstChild`: 첫번째 위젯
- `secondChild`: 두번째 위젯
- `crossFadeState`: 어떤 페이지를 보여줄지 컨트롤 함
- `duration`: Duration

### 📍 AnimatedContainer

- `decoration`: BoxDecoration안의 속성을 컨트롤함
- `duration`: Duration

### 📍 AnimatedOpacity

- `opacity`: 상태값으로 1 또는 0으로 컨트롤
- `duration`: Duration 사용
- `child`

### 📍 AnimationController

- Animation의 값 범위 및 상태를 control
- `late final` 키워드로 정의
- `vsync`: `TickerProvider`
  - widget_detail/ticker 참조

- `duration`
- `lowerBound`
- `upperBound`
- `value`: 시작값
- AnimationController의 event
  - `forward`
  - `reverse`
  - 위 두 동작이 수행될 때 addListener에서 감지함


📍 **Animation 적용 방식**

```dart
void _onToggleViedoPlay() {
	...
  _animationController.reverse(); or _animationController.forward(); // 1. event 수행 (anamation 값 변경)
```

📌 **Animation 적용 1: addListener**

```dart
...
@override
void initState() {
  super.initState();
  _animationController.addListener(() {															// 2. event 감지
    setState(() {});																								// 3. build(rendering)
  });
}
```

- `addListener`가 감지되면 `setState`를 통해 화면 다시 `rendering`

📌 **Animation 적용 2: AnimatedBuilder**

```dart
@override
Widget build(BuildContext context) {
...
  child: AnimatedBuilder(
    animation: _animationController,
    builder: (context, child) {
      return Transform.scale(
        scale: _animationController.value,
        child: child,
      );
    },
    child: AnimatedOpacity(
      opacity: _isPaused ? 1 : 0,
      duration: _duration,
      child: const FaIcon(
        FontAwesomeIcons.play,
        color: Colors.white,
        size: Sizes.size52,
      ),
    ),
  ),
	...
}
```

- `AnimatedBuilder`의 `animation` 필드의 `controller`로 인해 값 변경 감지
- 화면 전체를 다시 그리지 않고 `child`만 다시 그림