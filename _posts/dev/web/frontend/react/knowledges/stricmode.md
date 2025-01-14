### ✏️ StrictMode

📚 **index.js**

```react
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

- Strict Mode가 활성화 되어 있는 경우 개발 모드에서 컴포넌트가 두 번 렌더링 될 수 있음
- 컴포넌트 내에서 발생할 수 있는 부작용(side effects)을 감지하고 경고하기 위한 의도적인 동작
- 이 동작은 **개발 모드**에서만 발생하며, **프로덕션 모드**에서는 적용되지 않으니 성능에 영향을 주지 않음