### 📍 Column

> 자식을 세로 배열로 표시하는 위젯

- `height`
  - 부모의 제약이 있으면 부모의 높이
  - 부모의 제약이 없다면 세로축의 모든 공간을 차지함
- `width`
  - 부모의 제약이 있으면 부모의 너비
  - 부모의 제약이 없다면 children의 가장 큰 너비로 제한
- `mainAxisSize`
  - `min`: 자식 높이의 총 합 만큼
  - `max`: 가질 수 있는 높이 만큼 (default)
  - 단, 부모의 제약이 없을때만 적용됨
- `mainAxisAlignment`: 세로 축 정렬
  - default: `MainAxisAlignment.start` (세로 기준 처음부터)
- `crossAxisAlignment`: 가로 축 정렬
  - default: `crossAxisAlignment.center` (가로 기준 가운데)
- 자식의 크기를 늘리기 위해선 자식을 `Expanded`로 감싸야함
- 기본적으로는 스크롤 되지 않음
  - 자식 위젯이 `Column`이 가질 수 있는 공간을 넘어서면 오류
  - 스크롤을 위해 `ScrollView` 사용



### 📍 Row

> 자식을 가로 배열로 표시하는 위젯

- `height`
  - 부모의 제약이 있으면 부모의 높이
  - 부모의 제약이 없다면 children의 가장 큰 높이로 제한
- `width`
  - 부모의 제약이 있으면 부모의 너비
  - 부모의 제약이 없다면 가로 축의 모든 공간을 차지
- `mainAxisSize`
  - `min`: 자식 길이의 총 합 만큼
  - `max`: 가질 수 있는 길이 만큼 (default)
  - 단, 부모의 제약이 없을때만 적용됨
- `mainAxisAlignment`: 가로 축 정렬
  - default: `MainAxisAlignment.start` (가로 기준 처음부터)
- `crossAxisAlignment`: 세로 축 정렬
  - default: `crossAxisAlignment.center` (세로 기준 가운데)
  - `Column`과 다르게 높이를 지정해주지 않으면 티가 안날 수 있음
- 자식의 크기를 늘리기 위해선 자식을 `Expanded`로 감싸야함
- 기본적으로는 스크롤 되지 않음
  - 자식 위젯이 `Row`가 가질 수 있는 공간을 넘어서면 오류
  - 스크롤을 위해 `ScrollView` 사용
    - `scrollDirection`: `Axis.horizontal`



📌 **Expanded child**

- `Expanded child`: 부모의 남은 공간을 모두 차지
