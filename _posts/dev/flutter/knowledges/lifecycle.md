## 1. The App Lifecycle

### 1. App Lifecycle States

- `inactive`: 
- `paused`:
- `resumed`:
- `detached`:

```
https://velog.io/@tygerhwang/Flutter-Lifecycle%EC%95%B1-%EC%83%81%ED%83%9C-%EC%9D%B4%EB%B2%A4%ED%8A%B8-1%ED%8E%B8

https://yawarosman.medium.com/flutter-lifecycle-methods-an-in-depth-exploration-00b0747864bb

GPT야 쉽게설명해줘
```



## 2. Widget Lifecycle

### 1. Widget Lifecycle

1. `initState()`
   - 시점: widget이 widget tree에 삽입된 즉시 호출됨
   - 초기화 및 일회성 설정 작업에 사용됨
     - 스트림, 컨트롤러 이벤트 등록
2. `didChangeDependencies()`
   - 시점: 어떤 화면의 위젯이 상위 위젯(inheritedWidget)의 데이터나 설정에 의존하는 위젯에 의존하고 있다면, 상위 위젯이 바뀌었을때 호출됨
     - 상위 테마, 언어, 공유 데이터 같은 설정이 바뀌면 호출됨
   - 상위 위젯이 변경되었을 때 데이터를 다시 가져오거나 재초기화할 때 사용됨
3. `build()`
   - 시점: 화면을 새로 그릴때 호출, 현재 상태를 기반으로 화면에 보여질 UI를 정의
     - setState를 호출하면 build를 호출하게 됨
     - 부모 위젯이 다시 그려져 자식 위젯도 재구성될 때 호출
4. `didUpdateWidget()`
   - 시점: 부모 위젯이 다시 빌드되거나 properties가 변경되었을 때 호출됨
   - 위젯의 설정이 바뀌었을 때 호출되는 함수, 부모 위젯이 자식 위젯에 새 데이터를 보낼때 위젯에서 이 함수를 사용함
   - 상태는 유지되지만 속성이 변경되었을 때 반응함
5. `dispose`
   - 시점: 위젯이 영구적으로 제거될 때 호출
   - 리소스를 해제하거나 정리 작업 수행할 때 사용됨
     - 스트림이나 컨트롤러 같은 객체를 계속 사용시 메모리를 차지하게 되므로 해제를 위해 사용

