### CORS (Cross-Origin Resource Sharing)

**CORS**는 웹 브라우저가 다른 도메인에서 리소스를 요청할 때 발생하는 보안 문제를 해결하기 위한 메커니즘입니다. 기본적으로 웹 브라우저는 보안상의 이유로 다른 도메인에서 리소스를 요청하는 것을 제한합니다. CORS는 이러한 제한을 완화하여 특정 조건 하에서 다른 도메인에서 리소스를 요청할 수 있도록 합니다.

- **목적**: 다른 도메인에서 리소스를 안전하게 요청할 수 있도록 허용.

- **작동 방식**: 서버는 특정 출처(origin)에서 오는 요청을 허용할지 여부를 결정하고, 허용된 출처에 대해 응답 헤더를 통해 이를 알립니다.

- **설정 예시**:

  ```python:config/settings.py
  CORS_ALLOWED_ORIGINS = [
      "http://example.com",
      "http://anotherdomain.com",
  ]
  ```





### CORS 정책과 서로 다른 포트

CORS 정책에 따르면, **출처(origin)**가 다르다고 판단되는 경우에는 브라우저에서 요청을 차단할 수 있습니다.

📌 **출처**

> 웹 브라우저에서 리소르를 요청할 때, 요청이 발생한 출발점

- 출처는 다음 세 요소로 정의됩니다:

1. **프로토콜** (예: `http`, `https`)
2. **도메인** (예: `localhost`, `example.com`)
3. **포트 번호** (예: `3000`, `8000`)



두 요청의 도메인과 프로토콜이 같더라도, 포트가 다르면 서로 다른 출처로 간주됩니다. 예를 들어:

- **`localhost:3000`**와 **`localhost:8000`**은 포트 번호가 다르므로 서로 다른 출처로 인식됩니다.

이 경우 브라우저는 CORS 정책에 따라, 요청의 출처가 서버의 응답에 명시된 허용 출처 목록에 없으면 차단합니다.

### 해결 방법

1. **백엔드 서버에서 CORS 허용 설정**  
   백엔드 서버(`localhost:8000`)에서 `localhost:3000`에서 오는 요청을 허용하도록 설정해야 합니다. 이를 위해, Flask, Django, 또는 FastAPI 같은 백엔드 프레임워크에 CORS 설정을 추가합니다.

   예를 들어, Django에서 `django-cors-headers` 패키지를 사용해 다음과 같이 설정할 수 있습니다:

   ```python
   # settings.py
   INSTALLED_APPS = [
       ...
       'corsheaders',
       ...
   ]
   
   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       ...
   ]
   
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",
   ]
   ```

2. **프록시 설정 사용**  
   개발 환경에서 프록시 설정을 통해 요청을 같은 출처로 보내는 방법도 있습니다. 예를 들어, React 개발 서버 설정(`package.json`)에 프록시를 추가할 수 있습니다:

   ```json
   "proxy": "http://localhost:8000"
   ```

이렇게 설정하면, 브라우저는 요청을 차단하지 않고 `localhost:3000`에서 `localhost:8000`으로의 요청이 허용됩니다.
