## 1. Build Method와 State Instance의 생성 시점

> 화면에 처음 진입할 때, 객체가 메모리에 올라가는 것과 `build` 메서드가 동시에 수행됨 아래는 수행 순서

1. **객체 생성 및 초기화**:
   - `StatefulWidget`의 상태 객체(`State` 클래스의 인스턴스)가 생성되고, 메모리에 올라갑니다.
   - 이 시점에 `initState` 메서드가 호출됩니다.

2. **`build` 메서드 호출**:
   - 상태 객체가 초기화된 후, `build` 메서드가 호출되어 위젯 트리가 구성되고 화면에 그려집니다.

```dart
class _ImplicitAnimationsScreenState extends State<ImplicitAnimationsScreen> {
  // 클래스 멤버 변수
  final String title = "Implicit Animations";

  @override
  void initState() {
    super.initState();
    // 객체가 메모리에 올라갈 때 초기화 작업 수행
    // class 멤버 변수에 값 할당
    print("State 객체가 메모리에 올라갔습니다.");
  }

  @override
  Widget build(BuildContext context) {
    // build 메서드가 호출될 때마다 실행
    final size = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        title: Text(title), // 클래스 멤버 변수 사용
      ),
      body: Center(
        child: Column(
          children: [
            // size 변수 사용
            Text('Width: ${size.width}, Height: ${size.height}'),
          ],
        ),
      ),
    );
  }
}
```


위 예제에서, 다른 화면에서 이 화면으로 처음 진입할 때 다음과 같은 순서로 실행됩니다:

1. `_ImplicitAnimationsScreenState` 객체가 생성되고, `initState` 메서드가 호출됩니다.
2. `initState` 메서드가 완료된 후, `build` 메서드가 호출되어 화면이 그려집니다.

따라서, 객체가 메모리에 올라가는 것과 `build` 메서드가 호출되는 것은 초기 진입 시 거의 동시에 일어나는 과정입니다.

## 2. Build Method 변수와 class 멤버 변수

- build 메서드 안의 변수는 메서드가 호출될 때마다 새로 생성되며, 메서드가 끝나면 사라짐
- 반면, 클래스의 멤버 변수는 클래스 인스턴스가 존재하는 동안 유지됨
- 예를 들어, build 메서드 안의 size 변수는 build 메서드가 호출될 때마다 새로 계산

