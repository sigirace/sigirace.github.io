```
npm install react-helmet
npm i --save-dev @types/react-helmet
```

\+ Warning: Using UNSAFE_componentWillMount in strict mode is not recommended and may indicate bugs in your code.
React Helmet사용시 콘솔창에 위와 같은 경고창이 뜨시는 분들은 React Helmet 대신 React Helmet Async를 사용하시면 됩니다.
npm i react-helmet-async

**App.tsx**

```tsx
import { HelmetProvider } from "react-helmet-async";

<HelmetProvider>
<Router/>
</HelmetProvider>
```



```tsx
import { Helmet } from "react-helmet-async";

<Helmet>
<title>Chart</title>
</Helmet>
```

