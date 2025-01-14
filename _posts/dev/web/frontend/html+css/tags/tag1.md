📍 **lable**

> input과 연계하여 text를 클릭시 input 활성화

```html
<label for="minutes">Minutes</label>
<input id="minutes" placeholder="Minutes" type="number" min="0" />
<label for="hours">Hours</label>
<input id="hours" placeholder="Hours" type="number" min="0" />
```

- for과 id로 connect

📍 **select**

```html
<select>
  <option value="0">Minutes & Hours</option>
  <option value="1">KM & Miles</option>
</select>
```

- value는 string이여야 함

📍 **hr**

```html
<hr/>
```

- 헤드라인

📍 **JS 코드 작성**

```html
<div>
	<h1>
    Super Converter
  </h1>
  {
  code~
  }
</div>
```

- 중괄호를 사용해 코드 작성

📍 **header**

- 기본적으로 블록 요소로 화면 전체의 너비를 차지

📍 **div**

- 자식 요소의 너비에 따라 크기가 결정됨

### 📍 Nav

- Nav는 `ul`과 `li`로 구성됨
- `li`는 `a`를 가짐
- 단축키: n은 개수

> nav>ul>li*[n]>a
