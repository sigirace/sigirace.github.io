### 0. Project env

```
React 18
Router 5
```



### 1. project 생성

```
yarn create react-app your_project --template typescript
```



### 2. dependency

```json
"dependencies": {
    "@testing-library/jest-dom": "^5.14.1",
    "@testing-library/react": "^13.0.0",
    "@testing-library/user-event": "^13.2.1",
    "@types/jest": "^27.0.1",
    "@types/node": "^16.7.13",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "apexcharts": "^4.2.0",
    "gh-pages": "^6.2.0",
    "react": "^18.0.0",
    "react-apexcharts": "^1.7.0",
    "react-dom": "^18.0.0",
    "react-helmet": "^6.1.0",
    "react-helmet-async": "^2.0.5",
    "react-hook-form": "^7.54.2",
    "react-query": "^3.39.3",
    "react-router-dom": "^5.3.4",
    "react-scripts": "5.0.1",
    "recoil": "^0.7.7",
    "styled-components": "^6.1.13",
    "typescript": "^4.4.2",
    "web-vitals": "^2.1.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@babel/plugin-proposal-private-property-in-object": "^7.21.11",
    "@types/react-helmet": "^6.1.4",
    "@types/react-router-dom": "^5.3.3",
    "@types/styled-components": "^5.1.34"
  }
```

```
npm i
```



### 3. settings

📒 **.vscode/settings.json**

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```



### 4. init project

📒 **theme.ts**

```ts
import { DefaultTheme } from "styled-components";

const darkTheme: DefaultTheme = {
  textColor: "white",
  bgColor: "#2f3640",
  cardBgColor: "#f5f6fa",
  cardTextColor: "black",
  borderColor: "#f5f6fa",
  accentColor: "#44bd32",
};

const lightTheme: DefaultTheme = {
  textColor: "black",
  bgColor: "#f5f6fa",
  cardBgColor: "white",
  cardTextColor: "black",
  borderColor: "black",
  accentColor: "#44bd32",
};

export { darkTheme, lightTheme };
```

📒 **atom.ts**

```ts
import { atom } from "recoil";

export const isDarkAtom = atom({
  key: "isDark",
  default: false,
});

export const headerTitleAtom = atom({
  key: "headerTitle",
  default: "Coin Challenge",
});
```

📒 **routes/Home.tsx**

```tsx
export default function Home() {
  return <div>Home</div>;
}
```

📒 **Router.tsx**

```tsx
import { Switch, Route, HashRouter } from "react-router-dom";
import Home from "./routes/Home";

const Router = () => {
  return (
    <HashRouter basename={process.env.PUBLIC_URL}>
      <Switch>
        <Route path="/" exact component={Home} />
      </Switch>
    </HashRouter>
  );
};

export default Router;
```

📒 **index.tsx**

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { QueryClient, QueryClientProvider } from "react-query";
import { RecoilRoot } from "recoil";
const queryClient = new QueryClient();

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </RecoilRoot>
  </React.StrictMode>
);
```

📒 **index.css**

```css
@import url("https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400&display=swap");
```

📒 **App.tsx**

```tsx
import "./index.css";
import { createGlobalStyle, ThemeProvider } from "styled-components";
import Router from "./Router";
import { ReactQueryDevtools } from "react-query/devtools";
import { HelmetProvider } from "react-helmet-async";
import { darkTheme, lightTheme } from "./theme";
import { useRecoilValue } from "recoil";
import { isDarkAtom } from "./atom";

const GlobalStyle = createGlobalStyle`
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, menu, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
main, menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, main, menu, nav, section {
  display: block;
}
/* HTML5 hidden-attribute fix for newer browsers */
*[hidden] {
    display: none;
}
body {
  line-height: 1;
}
menu, ol, ul {
  list-style: none;
}
blockquote, q {
  quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
  content: '';
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
* {
  box-sizing: border-box;
}
body {
  font-family: 'Source Sans Pro', sans-serif;
  background-color:${(props) => props.theme.bgColor};
  color:${(props) => props.theme.textColor}
}
a {
  text-decoration:none;
  color:inherit;
}
`;

function App() {
  const isDark = useRecoilValue(isDarkAtom);
  return (
    <>
      <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
        <GlobalStyle />
        <HelmetProvider>
          <Router />
        </HelmetProvider>
      </ThemeProvider>
      <ReactQueryDevtools initialIsOpen={true} />
    </>
  );
}

export default App;
```



### 5. git flow

📌 **github**

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin [your project]
git push -u origin main
```

📌 **gitflow**

```
git flow init
git push origin --all
```







**github 배포**

