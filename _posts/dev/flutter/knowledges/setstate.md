## Q. setState의 호출 시점에 따른 차이

**첫 번째 코드**

```dart
void _onPanEnd(DragEndDetails details) {
 if (_direction == Direction.left) {
  setState(() {
   _showingPage = Page.second;
  });
 } else {
  setState(() {
   _showingPage = Page.first;
  });
 }
}
```

- **설명**: 여기서는 상태 변화 (_showingPage의 변경)가 setState 내부에 포함되어 있습니다. _direction에 따라 두 경우 각각에서 setState를 호출합니다.
- **재빌드 시점**: setState는 조건마다 한 번씩 호출되므로 _direction에 따라 위젯이 재빌드됩니다.
- **의미**: 상태 업데이트와 위젯 재빌드를 한 번에 처리합니다. 이는 Flutter에서 권장되는 상태 관리 방식입니다.
- **장점**: 코드의 의도가 명확하고 상태 변화가 즉시 적용되어 위젯이 재빌드됩니다.

**두 번째 코드**

```dart
void _onPanEnd(DragEndDetails details) {
 if (_direction == Direction.left) {
  _showingPage = Page.second;
 } else {
  _showingPage = Page.first;
 }
 setState(() {});
}
```

- **설명**: 여기서는 _showingPage의 상태를 먼저 업데이트하고 나서, 상태 변화와 상관없이 항상 빈 setState를 호출하여 위젯을 재빌드합니다.
- **재빌드 시점**: setState는 한 번만 호출되며, 어떤 상태 변화가 발생했든지 위젯은 한 번만 재빌드됩니다.
- **의미**: 상태 변화가 setState 바깥에서 이루어지고, setState는 단순히 위젯을 재빌드하기 위해 호출됩니다.
- **장점**: 상태 변화가 분리되어 명확히 보일 수 있지만, 코드의 의도가 덜 직관적일 수 있습니다.

**차이점 요약**

1. **첫 번째 코드**는 상태 업데이트가 setState 내부에서 이루어지기 때문에 코드의 의도가 명확하며, 관례에 따라 상태를 변경하는 것이 Flutter에서 권장됩니다.
2. **두 번째 코드**는 상태를 먼저 업데이트한 후 setState를 호출합니다. 이 방식도 작동은 하지만, 상태 변화와 위젯 재빌드의 연결이 덜 명확합니다.

**성능 차이**

- 대부분의 경우 성능 차이는 미미합니다. 하지만 첫 번째 방법은 조건에 따라 setState를 별도로 호출하기 때문에, 불필요한 재빌드를 방지할 수 있습니다.
- 두 번째 방법에서는 setState가 한 번만 호출되므로 약간 더 효율적일 수 있지만, 첫 번째 방법이 더 명확하고 관리하기 쉽습니다.



### ❤️‍🔥 권장: 첫 번째 방식이 더 명확하고 유지 관리하기 쉬운 코드 스타일입니다.