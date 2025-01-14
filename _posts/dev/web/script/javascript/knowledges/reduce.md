## 📍 Reduce

> ES6의 reduce 메서드는 배열의 모든 요소를 순회하면서 누적 계산을 할 수 있는 강력한 함수입니다. reduce는 배열을 단일 값으로 줄이거나 배열의 각 요소를 기반으로 객체를 만들고 합산하는 등의 작업을 수행할 때 유용하게 사용됩니다.



### 📌 reduce의 기본 사용법

- reduce는 배열의 각 요소에 대해 지정된 콜백 함수를 실행하고, 그 결과를 누적하여 최종 결과값을 반환합니다.

```js
const result = array.reduce((accumulator, currentValue, index, array) => {
 *// 누적 작업*
}, initialValue);
```

**Parameter**

- accumulator: 누적되는 값으로, 이전 반복의 결과를 유지합니다. initialValue가 제공되면 첫 번째 호출 시 initialValue로 설정됩니다.
- currentValue: 현재 배열 요소의 값입니다.
- index (optional): 현재 요소의 인덱스입니다.
- array (optional): 호출된 배열 자체입니다.

**initialValue**

- initialValue가 제공되지 않으면 배열의 첫 번째 요소가 accumulator로 설정되고, currentValue는 두 번째 요소부터 시작됩니다.
- initialValue를 지정하는 것이 안전하며, 특히 빈 배열에 대해 reduce를 호출할 때 유용합니다.



🌈 **예제: 배열의 합계 구하기**

```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(sum); *// 10*
```

- 여기서 accumulator는 매 반복마다 currentValue를 더하여 최종 합계를 반환합니다.
- initialValue는 0으로 설정되어 누적 합산이 제대로 작동합니다.



🌈 **예제: 배열에서 가장 큰 값 찾기**

```js
const numbers = [5, 12, 8, 130, 44];
const max = numbers.reduce((accumulator, currentValue) => Math.max(accumulator, currentValue));

console.log(max); *// 130*
```

- 각 요소를 순회하며 accumulator에 최대값을 유지하게 합니다.
- initialValue가 없으므로 첫 번째 요소 5가 accumulator의 초기값이 됩니다.



🌈 **예제: 객체 배열에서 특정 속성의 총합 구하기**

```js
const items = [
 { name: "apple", quantity: 2 },
 { name: "banana", quantity: 5 },
 { name: "orange", quantity: 3 }
];

const totalQuantity = items.reduce((accumulator, item) => accumulator + item.quantity, 0);

console.log(totalQuantity); *// 10*
```

- items 배열의 각 객체에서 quantity 값을 추출하여 총합을 계산합니다.

🌈 **예제: 배열을 객체로 변환하기**

```js
const fruits = ["apple", "banana", "orange"];

const fruitObject = fruits.reduce((accumulator, fruit) => {
 accumulator[fruit] = fruit.length;
 return accumulator;
}, {});

console.log(fruitObject); *// { apple: 5, banana: 6, orange: 6 }*
```

- 이 예제에서는 fruits 배열을 순회하면서 각 과일 이름을 키로, 이름의 길이를 값으로 하는 객체를 생성합니다.



### 📌 reduce의 장점

- 반복문을 사용하지 않고도 배열을 하나의 값으로 축약할 수 있습니다.
- **불변성 유지**: 기존 배열을 변경하지 않고 새로운 값을 반환하므로, 함수형 프로그래밍에 적합합니다.
- **유연성**: 숫자 합계뿐 아니라 객체 생성, 최대값 찾기 등 다양한 작업을 단순한 방식으로 처리할 수 있습니다.



### 💬 요약

- reduce는 배열의 요소를 누적하여 단일 값으로 변환하는 메서드로, 함수형 프로그래밍의 핵심입니다.
- 콜백 함수와 초기값을 통해 reduce를 다양한 방식으로 사용할 수 있으며, 특히 데이터 변환이나 집계 작업에 유용합니다.