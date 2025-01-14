## 📍 JS Event Loop



### 1. JS engine

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/dev/js/js_engine.png?raw=true" width="500" height="400"></p>

- **메모리 힙**: 메모리 할당이 일어나는 곳
  - **힙**: 구조화 되지 않은 넓은 메모리 영역으로 객체(변수, 함수 등)들이 담김
- **call stack**: 실행될 코드의 한줄 단위로 할당되어 실행 됨
  - js는 인터프리터로 동작하기에 한 줄 단위로 코드를 해석하고 수행
- **web api**: 비동기 처리를 담당
- **callback queue**: 비동기 처리가 끝난 후 실행되어야 할 콜백 함수가 차례로 할당 됨
  - 콜백 함수가 큐 안에 들어감
- **event loop**: 콜백 큐에 할당된 콜백 함수를 call stack에 할당해줌

### 2. call stack(sync)

📒 **example**

```js
function first(){
  second();
  console.log("첫번째");
}

function second(){
  third();
  console.log("두번째");
}

function third(){
  console.log("세번째");
}
first();
third();
```

- 콜 스택에는 먼저 모든 코드를 가지고 있는 `anonymous`가 담김
  - 호출 시 first()가 담김
  - 그다음 second(), third(), console.log("세번째") 가 담김
  - 이후 순차적으로 스택에 담기고 수행됨
- **stack overflow**: 콜스택 한계점을 초과한 경우

### 3. call stack(async)

📒 **example**

```js
console.log("시작");

setTimeout(function() {
  console.log("중간");
}, 3000);

console.log("끝");
```

- step1: 콜스택에 `anonymous`가 담김
- step2: console.log("시작")가 콜스택에 담기고 수행
- step3: settimeout 함수가 콜스택에 담김
  - 비동기 함수이니 실행되면서 web api로 이동
- step4: console.log("끝")이 콜스택에 담김 및 수행
- step5: `anonymous` 수행
- step6: web api에서 수행이 끝나면 콜백함수(익명함수로, console.log("중간")을 가지고 있음)를 callback queue로 이동
- step7: 이벤트루프가 call stack이 비어있는지 확인하고 익명함수를 콜백 큐에서 콜스택으로 넘김
- step8: 익명함수 안의 console.log("중간") 또한 callstack에 담김
- step9:  console.log("중간") -> 익명함수 수행 후
- step10: 종료

📌 **promise**

- promise는 기본적으로 동기임
- 그러나 then을 만나게 되면 엔진이 비동기로 인식
- 우선순위가 높아 콜백 큐에서 콜스택으로 먼저 이동

### 4. callback queue와 이벤트 루프

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/dev/js/callback_queue.png?raw=true" width="500" height="400"></p>

- **microtask queue(job queue)** > **animation frames** > **task queue(event queue)**
- 위의 우선순위를 대상으로 이벤트루프가 콜백스택에서 콜스택으로 넘김

