### 1. What is the syntax to type an array of booleans?

- boolean[]



### 2. In this code

```ts
const player: {
    name?:string,
    age:number
} = {
    name:"nico",
    age:44
}
```

- `name` is optional, `age` is required



### 3. For what do we use Type Aliases?

> 기존 타입에 새로운 이름을 부여하는 데 사용됩니다. 이를 통해 복잡한 데이터 구조를 간단히 표현하고 재사용할 수 있습니다.



### 4. What is the syntax to say that a function returns an array of strings?

- function name():string[]



### 5. Does the `readonly` from Typescript compile to JavaScript?

> **TypeScript의 `readonly`는 JavaScript로 컴파일되지 않습니다.** `readonly`는 개발 단계에서 타입 검사를 위해 사용되는 **TypeScript 전용 기능**입니다. TypeScript를 JavaScript로 컴파일할 때, `readonly`와 같은 타입 관련 키워드는 모두 제거됩니다.

- TypeScript에서 `readonly`는 객체의 속성을 초기화 이후에 변경할 수 없도록 지정하는 데 사용됩니다. 즉, **해당 속성은 읽기 전용**이 됩니다.

```ts
type User = {
    readonly id: number;
    name: string;
};

const user: User = { id: 1, name: "Alice" };

// 정상적으로 작동:
user.name = "Bob";

// TypeScript에서 오류 발생:
user.id = 2; // 오류: 'id'는 읽기 전용 속성이므로 값을 할당할 수 없습니다.
```



### 6. Why do we use Tuples for?

> TypeScript에서 **튜플(Tuple)**은 **정해진 길이와 타입 순서를 가진 배열**을 정의할 때 사용됩니다. 튜플은 배열과 비슷하지만, 각 요소의 타입과 위치가 고정되어 있어, 보다 엄격한 타입 검사를 제공합니다.

🌈 **튜플 예시**

```ts
function getUser(): [number, string] {
    return [1, "Alice"];
}

const [id, name] = getUser(); // id는 number, name은 string
```

📌 **배열**

> 배열은 **길이가 유동적이고 동일한 타입의 여러 값을 포함**합니다.

🌈 **배열 예시**

```ts
let mixedArray: (string | number)[] = [1, "Alice", 2];
mixedArray.push("Bob"); // 올바른 사용
mixedArray.push(3);     // 올바른 사용
```



### 7. What do we have to do before using a variable of type `unknown`?

> TypeScript에서 **`unknown` 타입**은 "아직 타입을 알 수 없는 값"을 나타내는 타입으로, 변수의 타입이 불확실할 때 사용됩니다. 하지만 `unknown` 타입의 변수는 **사용 전에 반드시 타입을 확인(type-checking)** 해야 합니다.
>
> `unknown` 타입은 **어떤 값이든 할당할 수 있지만, 직접 사용하거나 조작하려고 할 때는 타입을 확인해야만 사용할 수 있도록 강제**합니다. 이는 코드의 안전성을 높이고 런타임 오류를 방지하는 데 도움을 줍니다.



1. **`typeof` 연산자를 사용한 타입 확인**  
   `unknown` 타입을 사용하기 전에 `typeof`로 타입을 확인합니다.
   ```typescript
   let value: unknown;
   
   value = "Hello, TypeScript!";
   if (typeof value === "string") {
       console.log(value.toUpperCase()); // "HELLO, TYPESCRIPT!"
   }
   ```

2. **타입 단언(Type Assertion) 사용**  
   개발자가 타입을 확신하는 경우, 타입 단언을 사용하여 변수의 타입을 명시합니다.
   ```typescript
   let value: unknown = "Hello, TypeScript!";
   console.log((value as string).toUpperCase()); // "HELLO, TYPESCRIPT!"
   ```

3. **`instanceof` 연산자를 사용한 객체 타입 확인**  
   클래스나 객체 타입을 확인할 때는 `instanceof`를 사용합니다.
   ```typescript
   let value: unknown = new Date();
   
   if (value instanceof Date) {
       console.log(value.toISOString()); // ISO 날짜 문자열 출력
   }
   ```

4. **커스텀 타입 가드(Type Guard) 사용**  
   특정 조건을 정의하는 커스텀 함수로 타입을 확인할 수 있습니다.
   ```typescript
   function isString(value: unknown): value is string {
       return typeof value === "string";
   }
   
   let value: unknown = "Hello";
   if (isString(value)) {
       console.log(value.toUpperCase()); // "HELLO"
   }
   ```

---

### **`unknown`과 `any`의 차이점**
- **`unknown`**: 반드시 **타입 검증**을 통해야만 사용 가능 (더 안전)
- **`any`**: 어떤 타입이든 자유롭게 사용할 수 있으나, 타입 안전성이 없음

```typescript
let value: unknown;
let anyValue: any;

// unknown은 타입 확인 필요
if (typeof value === "number") {
    console.log(value + 1); // 타입 확인 후 사용 가능
}

// any는 아무 확인 없이 사용 가능 (위험)
console.log(anyValue + 1);
```



### 8. When do we use `never`?

> TypeScript에서 **`never` 타입**은 **절대 반환되지 않는 값**을 나타낼 때 사용됩니다. 즉, 함수가 정상적으로 종료되지 않거나 값을 반환하지 않는 경우에 주로 사용됩니다. `never`는 프로그램 흐름에서 **도달할 수 없는 상태**를 표현하는 데 유용합니다.

```ts
function throwError(message: string): never {
    throw new Error(message);
}
```

