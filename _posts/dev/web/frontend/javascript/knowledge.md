### ✏️ 비교 연산자

`==`와 `===`의 차이는 자바스크립트에서 매우 중요합니다.

- `==` (느슨한 동등 연산자): 두 값의 타입이 다르면 타입을 변환한 후 비교합니다.
- `===` (엄격한 동등 연산자): 두 값의 타입과 값이 모두 같아야 참으로 평가합니다.

예를 들어:
```javascript
console.log(1 == '1');  // true (타입 변환 후 비교)
console.log(1 === '1'); // false (타입과 값 모두 비교)
```

### ✏️ babel

```
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
```

-  Babel 라이브러리를 불러오는 코드입니다.
- Babel은 최신 JavaScript 코드를 구형 브라우저에서도 호환되도록 변환해주는 도구입니다.

```
<script type="text/babel">
```

- Babel을 사용하여 JSX 문법을 포함한 React 컴포넌트를 작성할 수 있게 해줍니다. 
- JSX는 JavaScript와 HTML을 결합한 문법으로, React에서 UI를 정의하는 데 사용됩니다.
