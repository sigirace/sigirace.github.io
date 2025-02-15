```
npm install react-query

or

yarn add react-query
```



**index.tsx**

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { ThemeProvider } from "styled-components";
import { theme } from "./theme";
import { QueryClient, QueryClientProvider } from "react-query";

const queryClient = new QueryClient();

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <App />
      </ThemeProvider>
    </QueryClientProvider>
  </React.StrictMode>
);
```



**App.tsx**

```tsx
import { ReactQueryDevtools } from "react-query/devtools";

...

function App() {
  return (
    <>
      <GlobalStyle />
      <Router />
      <ReactQueryDevtools initialIsOpen={true} />
    </>
  );
}

export default App;
```





### usage

**before**

```tsx
const [coins, setCoins] = useState<ICoin[]>([]);
const [loading, setLoading] = useState<boolean>(true);
useEffect(() => {
  (async () => {
    const response = await fetch("https://api.coinpaprika.com/v1/coins");
    const json = await response.json();
    setCoins(json.slice(0, 10));
    setLoading(false);
  })();
}, []);
```

**after**

```tsx
const { isLoading, data: coins } = useQuery<ICoin[]>("allCoins", fetchCoins);
```

- useQuery
  - unique Id
  - fetcher function



**api.ts**

```ts
const fetchCoins = async () => {
  return await fetch("https://api.coinpaprika.com/v1/coins").then(
    (response) => response.json()
  );
};

export { fetchCoins };
```

- fetcher 함수는 fetch promise를 return 해야함





### 결론

> useState를 통해 관리하던 loading와 useEffect를 통해 관리하던 data fetch를 useQuery 하나로 관리할 수 있음

- react query를 키를 기준으로 캐시에 저장하고 있기에 이전 화면으로 돌아가도 fetch하지 않을 수 있음