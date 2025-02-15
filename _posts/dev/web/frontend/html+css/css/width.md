### 📌 max-width

- 요소의 최대 너비를 제한
- 부모 컨테이너나 화면 크기에 따라 요소가 커질 수 있지만 max-width를 초과하지 않음
- 모바일에서 레이아웃이 너무 커지는 것을 방지함

🌈 **예시**

```css
.container {
  max-width: 600px;
  width: 100%;
  background-color: lightblue;
}
```

- 화면 크기가 **600px 이상**이면 container의 너비는 600px로 고정.
- 화면 크기가 **600px 미만**이면 container의 너비는 **100%**(즉, 부모 요소의 크기).



### 📌 min-width

- 요소의 최소 너비를 보장
- width 값이 min-width보다 작으면 min-width 크기로 유지
- 콘텐츠가 작아도 항상 일정 크기 이상을 유지해야 할 때 유용

🌈 **예시**

```css
.button {
  min-width: 150px;
  padding: 10px;
  background-color: orange;
}
```

- button의 너비가 150px 미만으로 줄어들지 않음.
- 내용물이 적어도 최소 150px 이상을 유지.



### 📌 max-width + min-width 함께 사용하기

🌈 **예시**

```css
.button {
  min-width: 100px;
  max-width: 300px;
  width: 50%;
  padding: 10px;
  background-color: green;
}
```

- button의 기본 너비는 **50%**
- 하지만 **100px보다 작아지지 않고, 300px보다 커지지 않음**.



### 🚀 결론

- max-width: **너무 커지는 걸 방지** → 콘텐츠가 화면을 꽉 채우지 않게 제한.
- min-width: **너무 작아지는 걸 방지** → 버튼, 입력 필드 등의 최소 크기 보장.
- **함께 사용하면 크기를 더욱 세밀하게 조정 가능**! 🚀