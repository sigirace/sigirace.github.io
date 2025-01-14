## 📍 Composition

💾 **데이터 정의**

```
u = {"id": 1, "firstName": "Gildong", "lastName": "Hong"}
```



📒 **초기 코드: 명령형**

```Js
function userDetail(u, caller){
  if(caller==="name"){
    //FullName Logic
  }else if (caller === "addr"){
    //appendAddr Logic
  }else if(caller === "remove"){
    //removedName Logic
  }
}
```

- 코드에 냄새가 나고 가슴이 아파야한다



📌 **함수 리팩토링**

```
const fullName = (user) => ({...user, fullName: '${user.firstName} ${user.firstName}'});
const appendAddr = (user) => ({...user, addre: "seoul"});
const removeNames = (user) => {
	delete user.firstName;
	delete user.lastName;
	return user;
}
```

📒 **Compose**

```js
const compose = (...fns) => (data) => {
  fns.reduce((c, fn) => fn(c), data)
}
```

- `(...fns)`: 함수들을 받는다

📌 **실행**

```js
const compose = (...fns) => (data) => {
  return fns.reduce((c, fn) => fn(c), data);
};
```



✏️ **ES5**

```js
function compose() {
  var fns = arguments;
  return function rfn(obj, index) {
    index = index || 0; 
    if (index < fns.length) {
      return rfn(fns[index](obj), index + 1);
    }
    return obj; // 모든 함수가 실행된 후 최종 결과 반환
  };
}

var result = compose(fullName, appendAddr, removeNames)(user); // 실행
```

- 괄호가 두개 붙을 수 있는 이유는 `compose`가 함수를 반환하기 때문

```js
var resultFunction = compose(fullName, appendAddr, removeNames);
var result = resultFunction(user);
```

- 나눠쓰면 이런식

