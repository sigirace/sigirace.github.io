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