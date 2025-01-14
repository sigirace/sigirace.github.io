### 📍 Scaffold

- **body**: 화면 전체를 차지하는 **width와 height**를 제공.

### 📍 SafeArea

- 상태바와 노치 등 기기에서 안전하지 않은 영역을 피하여 **가려지지 않는 width와 height**를 설정.

### 📍 Padding

- **width와 height를 결정하지 않음**.
- 부모의 영역에서 **패딩 공간만을 설정**하여 내부 여백을 추가함.

### 📍Wrap

- child를 가로로 배치하고 한줄에 다 안들어가면 다음줄로 넘어감
- `runspacing`: 세로 간격 조정
- `spacing`: 가로간격 조정

### 📍Form

- **key**: global formKey 필요 (flutter > knowledges > widget_detail > form.md)
- **key.currentState**
  - `validate()`: Form에 포함된 모든 TextFormFiled의 validator 함수 호출
  - `save()`: TextFormField의 onSaved 콜백 호출

### 📍 Expanded

- Expanded는 Flex 위젯(예: Column, Row를 부모로 가짐) 안에서만 동작하므로, Column이 반드시 부모가 제공하는 남은 공간을 모두 차지하게 합니다.
- Column **또는** Row **위젯이 자식 위젯들을 배치할 때**
  - 먼저, 높이(Column의 경우)나 너비(Row의 경우)가 명확하게 지정된 위젯들이 먼저 배치됩니다.
  - 고정 크기의 위젯들이 차지하고 남은 공간이 얼마인지 계산합니다.

- Expanded **위젯이 있는 경우**:
  - 남은 공간을 Expanded 위젯에 할당하며, 여러 개의 Expanded 위젯이 있을 경우 flex 속성에 따라 비율로 나누어 차지하게 됩니다.
  - flex 값이 없는 경우 기본적으로 1로 설정되며, 동일한 크기만큼 공간을 나눕니다.

🌈 **예시**

```dart
Column(
  children: <Widget>[
    Container(
      color: Colors.blue,
      height: 100,
      width: 100,
    ),
    Expanded(
      child: Container(
        color: Colors.amber,
        width: 100,
      ),
    ),
    Container(
      color: Colors.blue,
      height: 100,
      width: 100,
    ),
  ],
)
```

- 첫 번째와 세 번째 Container는 각각 높이가 100으로 고정되어 있으므로, 이 두 위젯이 먼저 배치됩니다.
- 이후 남는 공간이 있을 경우 Expanded가 그 공간을 전부 차지합니다.
