## 📍 Arguments

> arguments 객체는 함수 내부에서 사용할 수 있는 유사 배열 객체로, 함수에 전달된 모든 인수를 담고 있습니다.

- ES5 이전과 이후로 arguments의 사용 방식에는 차이가 있으며, ES6부터는 더 나은 대체 방법인 **전개 연산자(...)**가 도입되었습니다.



### 📌 ES5 이전의 arguments 객체

- **정의**: arguments는 모든 함수 내부에 자동으로 생성되는 유사 배열 객체로, 함수 호출 시 전달된 인자들이 저장됩니다.
- **유사 배열**: arguments는 배열이 아니지만, length 속성으로 인자 개수를 확인할 수 있고, 배열처럼 인덱스를 사용해 인자에 접근할 수 있습니다. 다만, forEach, map 등의 배열 메서드는 사용할 수 없습니다.
- **함수 매개변수 이름과 연동**: arguments는 매개변수와 직접 연동되어, 매개변수 값이 변경되면 arguments의 해당 인자 값도 함께 변경됩니다.



🌈 **예시**

```js
// case1
function example1(a, b) {
 console.log(arguments[0]); 
 console.log(arguments[1]); 
}

//case2
function example2() {
 console.log(arguments[0]); 
 console.log(arguments[1]); 
}

example1(1, 2);
example2(1, 2);
```

```
1
2
1
2
```

- 두 함수 example1과 example2의 실행 결과가 같은 이유는, arguments **객체는 함수의 매개변수와 상관없이, 함수에 실제로 전달된 인수를 모두 포함하기 때문**입니다.
- arguments 객체는 함수가 호출될 때 전달된 모든 인수를 담고 있으며, 함수의 매개변수와 직접적인 관계가 없습니다.



### 📌 arguments의 유사 배열 성질 해결

> ES5 이전에는 배열 메서드를 사용할 수 없었기 때문에, 배열 메서드가 필요할 경우 Array.prototype.slice.call(arguments)로 arguments를 배열로 변환했습니다.

```js
function example() {
 var args = Array.prototype.slice.call(arguments); *// 배열로 변환*
 console.log(args); *// [1, 2, 3]*
}

example(1, 2, 3);
```



### 📌 ES6 이후의 변화와 전개 연산자(...args)

> ES6(ECMAScript 2015) 이후, **전개 연산자**(...)가 도입되면서 arguments 객체를 사용하는 대신 **더 명확하고 유연한 방식**으로 함수 인자를 다룰 수 있게 되었습니다.

- **전개 연산자(**...args**) 도입**: 함수 매개변수에서 ... 연산자를 사용하여 여러 인자를 배열 형태로 수집할 수 있습니다.
- **유사 배열이 아닌 배열**: ...args로 생성된 매개변수는 배열이므로, map, forEach와 같은 배열 메서드를 사용할 수 있어 더 직관적입니다.
- **매개변수와 연동되지 않음**: 전개 연산자로 수집된 인자 배열은 매개변수와 직접 연동되지 않으므로, 독립적인 배열로 유지됩니다.



**1. 함수의 매개변수 부분에서 ...args 사용 (Rest Parameter)**

- 함수의 매개변수 부분에서 ...args를 사용하면, **Rest Parameter**로써 여러 개의 인자를 배열로 수집합니다.
- 이 경우, ...args는 함수에 전달된 모든 인수를 배열로 받아옵니다.

🌈 **예시**

```jS
function example(...args) {
  console.log(args); // 모든 인자를 배열로 수집
}

example(1, 2, 3); 
// 출력: [1, 2, 3]
```

**2. 함수 호출 시 전개 연산자 사용 (Spread Operator)**

- 함수를 호출할 때 **전개 연산자를 사용하여 배열을 개별 인수로 펼쳐** 전달할 수도 있습니다.
- 이 경우 ...는 배열의 각 요소를 하나씩 나열된 인수로 전달합니다.

🌈 **예시**

```js
function sum(a, b, c) {
  return a + b + c;
}

const numbers = [1, 2, 3];
var result = sum(...numbers);
console.log(result);
// 출력: 6 (numbers 배열이 개별 인수로 전달됨)
```


