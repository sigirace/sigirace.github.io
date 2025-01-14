https://aws.amazon.com/ko/blogs/korea/what-happens-when-you-type-a-url-into-your-browser/



### 📍 WS-WAS 연계

1. **Nginx를 서버 앞단에 배치**:
   - Nginx가 **80번 포트**에서 클라이언트 요청을 수신.
   - 사용자는 `https://domain.com`으로 접속.

2. **사용자의 요청 처리 흐름**:
   - **첫 요청**:
     - Nginx가 **index.html**을 제공하여 브라우저에 렌더링.
     - 사용자의 화면에는 **index.html**이 출력됨.
   - **추가 요청**:
     - 사용자 요청은 URL 구조를 기준으로 Nginx에서 라우팅.

3. **Nginx의 역할**:
   - **정적 파일 제공**: 
     - `80`번 포트에서 `index.html` 서비스.
   - **URL 네임스페이스 기반 요청 라우팅**:
     - `/api/users`처럼 URL에 따라 요청을 적절한 서버로 전달.
     - 예:  
       - `/node/...` → **Node.js 서버 (9001번 포트)**로 전달.  
       - `/flask/...` → **Flask 서버 (9002번 포트)**로 전달.

4. **Node.js와 Flask 서버**:
   - Node.js: `9001번 포트`에서 실행.
   - Flask: `9002번 포트`에서 실행.

5. **프록시와 방화벽**:
   - **프록시**: Nginx가 요청을 **Node.js** 또는 **Flask 서버**로 전달하는 통로 역할.
   - **방화벽**: Nginx 앞단에 배치되어 보안 강화.

---

#### 정리된 요청 흐름:

1. 사용자는 `https://domain.com`에 접속.
2. Nginx가 정적 파일(`index.html`)을 반환하여 브라우저에 표시.
3. 브라우저에서 `/api/users`와 같은 API 호출 발생.
4. Nginx가 URL 기준으로 요청을 Node.js(9001) 또는 Flask(9002) 서버로 전달.
5. Node.js 또는 Flask 서버가 요청을 처리하여 응답.

---

#### 특징:
- Nginx가 **요청 라우팅**과 **정적 파일 제공**을 담당하여 서버 부하 분산.
- 애플리케이션 서버(Node.js, Flask)는 각각 고유한 포트에서 동작.
- 확장성과 보안(방화벽) 강화.







### 📍 Nginx의 주요 역할

1. **리버스 프록시**:

   - 클라이언트 요청을 받아 백엔드 서버(Node.js, Flask, Spring, Tomcat 등)로 전달.
   - 백엔드 서버가 처리한 결과를 다시 클라이언트에게 반환.
   - 이를 통해 클라이언트는 Nginx만 접촉하고 백엔드 서버의 상세 정보는 알 수 없음.

   #### 예:

   - 클라이언트 요청:
     `https://example.com/api/data`
   - Nginx가 이를 받아 백엔드 서버로 전달:
     `http://backend-server:8080/api/data`

2. **로드 밸런싱**:

   - 여러 백엔드 서버에 트래픽을 분산시킴.
   - 동일한 서비스가 여러 서버(예: Node.js 인스턴스)에서 실행될 경우 부하를 효율적으로 나눔.
   - **Round-robin**, **Least connections** 등 다양한 방식 지원.

3. **정적 파일 제공**:

   - HTML, CSS, JS 등 **정적 파일**을 직접 제공.
   - 백엔드 서버의 부하를 줄이는 역할.

4. **SSL/TLS 종료**:

   - HTTPS 요청을 처리하여 SSL/TLS 암호화 및 복호화를 수행.
   - 백엔드 서버는 일반 HTTP 통신만 하도록 설정 가능.

5. **캐싱**:

   - 정적 콘텐츠 또는 일부 동적 콘텐츠를 캐싱하여 빠르게 제공.
   - 백엔드 서버와의 통신을 줄여 성능 향상.

6. **웹소켓 지원**:

   - 실시간 통신이 필요한 경우 WebSocket 프로토콜을 지원.
