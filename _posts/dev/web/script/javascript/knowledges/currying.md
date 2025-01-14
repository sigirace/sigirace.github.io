## 📍 Currying



- 중국집에 가면 중국집 메뉴를 주문하고, 이탈리아 레스토랑에 가면 이탈리아 메뉴를 주문함
- 그런데 주문을 위해서는 중국집, 이탈리아 레스토랑에 진입해야함
- 즉 함수가 두개가 됨
  - 식당에 들어가는것
  - 주문하는것

```js
const order = (store) => (menu) => console.log('${store}에서 ${menu}를 주문했다');
```

- `=>`가 두개나오면 currying

```js
oder('중국집')('자장면');
```

- 실행



✏️ **ES5**

```js
function order(store){
	return function(menu){
    console.log('${store}에서 ${menu}를 주문했다');
  }
}
```



✏️ **실행코드 중복 방지**

```js
const orderCh = order('중국집');
orderCh('자장면');
orderCh('짬뽕');
```