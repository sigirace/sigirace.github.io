### 📍 VisibilityDetector

- 화면에 보이는 영역을 `visibilityinfo`로 나타냄
- `key`: 현재 화면 index
- `onVisibilityChanged`: 화면의 변화



### 📍GestureDetector

- `onTap`: 콜백을 기대함, 이벤트가 발생할 때 함수를 호출하도록 설정해야함
  - 즉, 함수의 실행인 `function()`이 아닌 참조인 `function`을 사용
  - 프로퍼티가 함수를 받는지 확인하고 `void Function()?`일 경우 참조 전달
  - 포커스아웃: () => FocusScope.of(context).unfocus()
- `onPanUpdate`: void Function(DragUpdateDetails) -> drag 시 액션
  - `delta`: offset
    - 0보다 크면 오른쪽
    - 0보다 작으면 왼쪽

- `onPanEnd`: void Function(DragEndDetails) -> drag가 끝난 후

📌 **Pan**

**주의점**

- Fade 기능을 사용시 GestureDetector가 최상단으로 와야함

**Property**

```dart
void Function(DragUpdateDetails)? onPanUpdate
void Function(DragEndDetails)? onPanEnd
```









