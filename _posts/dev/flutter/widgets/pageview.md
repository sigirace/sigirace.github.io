### 📍 Pageview

- `pageSnapping`: Auto Animate page transitions
  - (default) true
- `scrollDirection`: 스크롤 방향
- `onPageChanged`: 페이지 변경시 수행할 call back
- `controller`: `PageController`



📌 **builder**

> widget을 만들지만 child 들을 모두 동시에 render하지 않음

- `itemBuilder`: 위젯을 반환하는 함수
  - required Widget? Function(BuildContext, int) itemBuilder
  - `context`: 어떤 화면에 반환할 것인가
  - `int`: index



📌 **pageController**

- `animateToPage`: 다른 화면으로 이동
- `nextPage`: 다음 화면으로 이동



