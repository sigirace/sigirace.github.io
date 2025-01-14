```
npm i styled-components
```

**ts**

```
npm i styled-components
npm i --save-dev @types/styled-components
```





### 2.7 Themes

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { ThemeProvider } from "styled-components";
import App from "./App";

const darkTheme = {
  textColor: "whitesmoke",
  backgroundColor: "#111",
};

const lightTheme = {
  textColor: "#111",
  backgroundColor: "whitesmoke",
};

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={darkTheme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
```

- ThemeProvider는 theme props를 받음
- App이 ThemeProvider 안에 있기에 컴포넌트 내에서 접근할 수 있음
- 여러 Theme들의 property가 같아야함

```javascript
const Father = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: ${props => props.theme.backgroundColor};
  color: ${props => props.theme.textColor};
`;
```



### Theme

- Theme은 dark/light mode를 사용할 수 있게함
- 타입스크립트와 styled components 테마를 연결
- type definition 설치

```
npm i --save-dev @types/styled-components
```

- 타입스크립트에게 styled components가 무엇인지에 대해 설명해주는 파일
  - 해당 패키지 github index.d.ts에 있음
- 위 파일은 다운로드받아서 타입스크립트에 설명하고 있지만 Theme을 사용하기 위해 확장이 필요
- 따라서 선언 파일을 만들어야함

📒 **styled.d.ts**

```ts
import 'styled-components';


declare module 'styled-components' {
  export interface DefaultTheme {
    textColor: string;
    backgroundColor: string;
  }
}
```

- 위 파일에서 styled-components를 오버라이드할거임





