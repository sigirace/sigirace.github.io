### 1. JavaScript is a type safe language

- no



### 2. What happens if we run this code in JS:

```js
["hello"]+{hi:1}
```

- It will run

```
'hello[object Object]'
```



### 3. What is a runtime error?

- An error that happens while the code runs



### 4. What is Typescript compiled to?

- JavaScript Code



### 5. Is this valid Typescript code?

```ts
const kimchi = {
    맛있어: true
}
```



### 6. We always have to specify a type for our variables in Typescript.

- No, Typescript can infer it sometimes

TypeScript에서 변수에 타입을 명시하는 것은 **반드시 필요한 것은 아닙니다.** TypeScript는 강력한 **타입 추론(type inference)** 기능을 제공하기 때문에, 많은 경우 타입을 명시하지 않아도 됩니다.



🌈 **타입 명시 없이 작성한 예제**

```ts
const kimchi = {
  맛있어: true
};
```

이 경우 TypeScript는 kimchi의 타입을 자동으로 추론합니다:

```
{ 맛있어: boolean }
```



🌈 **타입을 명시한 경우**

필요하다면 명시적으로 타입을 지정할 수도 있습니다:

```ts
const kimchi: { 맛있어: boolean } = {
  맛있어: true
};
```



💡 **언제 타입을 명시해야 할까?**

1. 복잡한 객체나 API 규격이 필요한 경우: 추론된 타입이 구조를 완벽히 표현하지 못할 때, 특히 큰 객체나 인터페이스를 정의할 때 명시적으로 작성하는 것이 좋습니다.
2. 함수의 매개변수나 반환값: 함수의 인자나 반환 타입은 명시적으로 작성하는 것이 권장됩니다. 이를 통해 함수 사용 시 더 명확하고 예측 가능한 동작을 보장할 수 있습니다.
3. 추론이 실패하는 경우: TypeScript가 타입을 정확히 추론하지 못하거나 any로 추론될 때는 명시적으로 타입을 지정하는 것이 안전합니다.



📌**타입 추론이 충분한 경우**

대부분의 경우, 특히 간단한 변수나 상수에서는 TypeScript의 추론 기능을 믿고 타입을 생략해도 문제가 없습니다. 예를 들어, 위의 kimchi 객체는 타입을 명시하지 않아도 TypeScript가 정확히 추론합니다.



