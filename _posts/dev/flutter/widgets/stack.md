### 📍 Stack

- **`Align` 위젯을 child로 가질 수 있음**.
- **`Align` 위젯은 `Stack` 내에서 자식의 위치를 조정할 수 있음**.
- 버튼을 만들 때 아이콘과 텍스트의 **고유 여백을 무시하거나 수정할 때 유용함**.
- **clipBehavior**: 스택 내의 positioned Widget이 있을 경우 부모인 stack의 크기를 벗어날때 잘라낼지 결정하는 것



📌 **clipBehavior type**

> stack의 위치에서 offset 적용 뒤, 기존 범위를 벗어나는 것에 대한 처리

- **Clip.none**: 자르지 않음
- **Clip.hardEdge**: 부모의 경계를 벗어나면 잘라냄, 성능 우선
- **Clip.antiAlias**: 부드럽게 잘라냄
- **Clip.antiAliasWithSaveLayer**: 부드럽게 잘라내지만 뭔가 더 복잡한 처리로 시각적으로 효과가 좋게함, 성능은 떨어짐



### 📍 OffStage

- Stack 내에서 여러 화면을 겹쳐서 띄워놓음
- **offstage**: true일 경우 보이게 됨
- **child**: 띄워놓을 화면



### 📍 Positioned

- left/ right/ top/ bottom: 만큼 이동함
- `fill`: 화면 전체를 채움
  - `GestureDetector`와 함께 쓸때는 `Stcak` 내에서 `fill`이 부모가 되어야 함
  - `Stack`된 화면이 여러개일 때 아래 층의  `Gesture`를 감지하기 위해서는 `IgnorePointer` 사용

