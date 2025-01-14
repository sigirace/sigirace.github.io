### 1. A `readonly` class property in TS will also be `readonly` in JS

- no

> TypeScript의 readonly 키워드는 **타입 수준에서만 적용**되며, 컴파일 시 **오류를 잡는 역할**을 합니다. JavaScript로 변환되면 readonly 키워드는 제거되며, 속성은 일반적인 속성처럼 동작합니다.

🌈 **예제: TS**

```ts
class Example {
  readonly name: string;

  constructor(name: string) {
    this.name = name;
  }
}

const instance = new Example("TypeScript");
instance.name = "JavaScript"; // TypeScript에서 오류: 'name'은 읽기 전용 속성이므로 수정할 수 없습니다.
```

🌈 **예제: JS**

```js
class Example {
  constructor(name) {
    this.name = name;
  }
}

const instance = new Example("TypeScript");
instance.name = "JavaScript"; // JavaScript에서는 문제가 없고, 속성이 수정됩니다!
```



### 2. `abstract` class will become a normal class in JS

- Yes

> **TypeScript의** abstract **클래스**는 JavaScript로 컴파일될 때 **일반 클래스**로 변환됩니다. 즉, TypeScript에서 abstract 키워드는 **컴파일 타임에서만 존재**하며, JavaScript로 변환될 때 제거됩니다.

🌈 **예제: TS**

```ts
abstract class Shape {
  abstract getArea(): number; // 추상 메서드, 하위 클래스에서 구현 필요

  printName(): void {
    console.log("This is a shape.");
  }
}

class Circle extends Shape {
  radius: number;

  constructor(radius: number) {
    super();
    this.radius = radius;
  }

  getArea(): number {
    return Math.PI * this.radius * this.radius;
  }
}

const circle = new Circle(5);
console.log(circle.getArea()); // 78.53981633974483
```

🌈 **예제: JS**

```js
class Shape {
  printName() {
    console.log("This is a shape.");
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  getArea() {
    return Math.PI * this.radius * this.radius;
  }
}

const circle = new Circle(5);
console.log(circle.getArea()); // 78.53981633974483
```

