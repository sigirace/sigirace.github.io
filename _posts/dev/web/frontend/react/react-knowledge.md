### ✏️ StrictMode

📚 **index.js**

```react
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

- Strict Mode가 활성화 되어 있는 경우 개발 모드에서 컴포넌트가 두 번 렌더링 될 수 있음
- 컴포넌트 내에서 발생할 수 있는 부작용(side effects)을 감지하고 경고하기 위한 의도적인 동작
- 이 동작은 **개발 모드**에서만 발생하며, **프로덕션 모드**에서는 적용되지 않으니 성능에 영향을 주지 않음

### ✏️ State

React에서 `state`가 변경될 때, **state가 변경된 컴포넌트**와 그 **하위 컴포넌트**들이 다시 렌더링됩니다.

React는 내부적으로 **Virtual DOM**을 사용하여 변경 사항을 효율적으로 처리합니다:
1. `setState`나 `useState`로 상태가 변경되면, React는 Virtual DOM에서 이전 상태와 현재 상태를 비교합니다.
2. 변경된 부분만을 찾아 실제 DOM에 반영하여, 필요한 부분만 다시 렌더링합니다.
3. 상태가 변경된 컴포넌트의 **리액트 트리 구조**에서 해당 컴포넌트와 하위 컴포넌트들이 다시 렌더링되지만, 형제 컴포넌트나 상위 컴포넌트는 다시 렌더링되지 않습니다.

따라서 **state**가 변경되면 **해당 state를 사용하는 컴포넌트와 그 하위 컴포넌트들**만이 영향을 받게 됩니다.



### ✏️ Rendering

**렌더링**된다는 것은 해당 컴포넌트의 **함수가 다시 호출**되어 컴포넌트의 JSX 코드가 **다시 수행**된다는 의미입니다.

자세히 설명하자면:

1. 컴포넌트가 렌더링될 때, 그 컴포넌트 함수의 코드가 처음부터 다시 실행됩니다.
2. 그 결과로 **JSX가 다시 계산**되고, React는 **Virtual DOM**에서 이전 결과와 새로운 결과를 비교합니다.
3. 변화가 있을 경우, React는 **실제 DOM에 필요한 부분만 업데이트**합니다. 이를 **리액트의 효율적인 렌더링 방식**이라고 합니다.

### 예시로 설명:

```jsx
function App() {
  const [counter, setCounter] = useState(0);

  return <h1>{counter}</h1>;
}
```

`setCounter`가 호출되어 `counter`의 값이 변하면:
- **`App` 함수가 다시 호출**됩니다.
- 내부의 JSX가 **다시 계산**되어, `<h1>{counter}</h1>` 부분이 새로운 값으로 렌더링됩니다.

즉, **렌더링**된다는 것은 해당 컴포넌트의 함수가 다시 실행되면서 컴포넌트의 새로운 상태에 맞게 **UI를 재구성**하는 과정입니다.



### ✏️ Map

React.js의 map안에서 component를 render할 때 key를 사용해야함

⛔️ **issue**

```
App.js:23 Warning: Each child in a list should have a unique "key" prop.
```

- key 사용 안할시 에러

✏️ **Async Undefined**

`data`가 `undefined`일 수 있는 이유는 `useQuery` 훅이 비동기적으로 데이터를 가져오기 때문입니다. 데이터가 로드되기 전에 컴포넌트가 렌더링되면 `data`는 초기 상태로 `undefined`가 될 수 있습니다. 이 경우 `data.map`을 호출하면 오류가 발생합니다.

`data?.map`을 사용하면, `data`가 `undefined`일 경우 `map` 메서드가 호출되지 않도록 안전하게 처리할 수 있습니다. 즉, `data`가 `undefined`일 때는 `undefined`를 반환하고, `data`가 유효한 배열일 때만 `map`을 실행합니다.

아래는 수정된 코드입니다:

```typescript:src/routes/Home.tsx
      {data?.map((room) => (
        <Room
          key={room.pk}
          imageUrl={room.photos[0].file}
          name={room.name}
          rating={room.rating}
          city={room.city}
          country={room.country}
          price={room.price}
        />
      ))} 
```

이렇게 하면 `data`가 `undefined`일 때는 아무것도 렌더링하지 않게 되어 오류를 방지할 수 있습니다.

✏️ **React Query의 캐시**

React Query의 캐시는 브라우저의 메모리 내에 저장됩니다. React Query는 내부적으로 JavaScript 객체를 사용하여 쿼리 키를 기반으로 데이터를 캐시합니다. 이 캐시는 애플리케이션의 생명 주기 동안 유지되며, 다음과 같은 방식으로 관리됩니다:

1. **메모리 캐시**: React Query는 기본적으로 메모리 내에서 데이터를 저장합니다. 이는 애플리케이션이 실행되는 동안만 유효하며, 페이지를 새로 고침하거나 애플리케이션을 종료하면 캐시는 사라집니다.

2. **쿼리 키**: 각 쿼리는 고유한 쿼리 키를 가지며, 이 키를 통해 캐시된 데이터를 식별하고 접근할 수 있습니다. 예를 들어, `queryKey: ["rooms"]`는 `rooms` 데이터를 식별하는 데 사용됩니다.

3. **캐시 관리**: React Query는 캐시된 데이터를 자동으로 관리합니다. 데이터의 유효성을 검사하고, 필요에 따라 데이터를 새로 고치거나 만료시키는 기능을 제공합니다. 이를 통해 최신 데이터를 유지할 수 있습니다.

4. **DevTools**: React Query DevTools를 사용하면 현재 캐시된 쿼리와 상태를 시각적으로 확인할 수 있습니다. 이를 통해 캐시의 내용을 쉽게 모니터링하고 디버깅할 수 있습니다.

이러한 방식으로 React Query는 효율적으로 데이터를 캐시하고 관리하여 애플리케이션의 성능을 향상시킵니다.



