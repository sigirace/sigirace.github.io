### 📍 Call Signature

> **Call Signature는 함수의 입력(매개변수)과 출력(반환값)의 타입을 정의하는 타입 서명입니다.** 정의한 Call Signature에 맞게 함수의 구현부를 작성하면 TS는 이를 기반으로 타입 검사를 수행합니다.

📌 **Call Signature의 정의와 구현**

1. **Call Signature 정의**  
   먼저 함수의 입력과 출력 타입을 정의합니다.

   ```typescript
   type AddFunction = (a: number, b: number) => number;
   ```

   여기서 `AddFunction`은 두 개의 `number` 타입 매개변수를 받아 `number` 타입을 반환하는 함수의 Call Signature를 정의한 것입니다.

2. **구현부 작성**  
   이 Call Signature에 따라 실제 함수 구현을 작성합니다.

   ```typescript
   const add: AddFunction = (a, b) => {
       return a + b;
   };
   ```

   - `add` 함수는 `AddFunction` 타입을 따르기 때문에 `a`와 `b`는 반드시 `number` 타입이어야 하며, 반환값도 `number`이어야 합니다.
   - 만약 타입을 따르지 않으면 TS에서 컴파일 오류가 발생합니다.





### 1. What is `call signature`?

- Is the type of the qrguments and return value of a function



### 2. A call signature has the implementation of the function.

- No



### 3. Call Signatures will be compiled into Javascript

- No

- Javascript는 concept of types를 갖지 않음



### 4. We can use the same call signature for multiple functions.

- YES

TypeScript에서 Call Signature는 함수의 타입 정의를 나타내며, 이 타입 정의는 여러 함수에서 재사용할 수 있습니다. 이렇게 하면 같은 매개변수와 반환 타입 구조를 가진 함수들에 대해 일관성을 유지할 수 있습니다.

---

### 🌈 예제

#### 1. Call Signature 정의
```typescript
type Operation = (a: number, b: number) => number;
```

위에서 `Operation`은 두 개의 `number`를 입력받아 `number`를 반환하는 함수의 Call Signature입니다.

#### 2. 여러 함수에서 재사용
```typescript
const add: Operation = (a, b) => a + b;
const subtract: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
```

- `add`, `subtract`, `multiply` 함수는 모두 동일한 Call Signature인 `Operation`을 사용합니다.
- 이로 인해 매개변수 타입과 반환 타입이 동일한지 TS가 자동으로 검사합니다.

