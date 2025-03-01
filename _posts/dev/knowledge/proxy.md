### Proxy

> 클라이언트와 서버 사이에서 중개 역할을 하는 서버 또는 소프트웨어

- 보안, 익명성 유지, 속도 향상, 콘텐츠 필터링 등 다양한 용도로 사용

**📌 1. 프록시의 기본 개념**

**✅ 기본적인 데이터 흐름**

```
[클라이언트] → (요청) → [프록시 서버] → (요청) → [원격 서버]
[클라이언트] ← (응답) ← [프록시 서버] ← (응답) ← [원격 서버]
```

**📌 2. 프록시의 종류**

> 목적에 따라 프록시의 종류가 달라짐

**✅ 1) 정방향 프록시(Forward Proxy)**

- 사용자가 특정 웹 사이트에 직접 접속하지 않고 프록시 서버를 통해 우회
- VPN, 인터넷 접근 제어

**✅ 2) 역방향 프록시(Reverse Proxy)**

- 사용자가 특정 웹 서버에 요청을 보낼때, 서버 앞에 프록시 서버를 두어 요청을 대신 처리
- 부하 분산, 보안 강화, 캐싱 등
- Nginx, Apache, HAProxy 등



🌈 **예제: Nginx를 이용한 역방향 프록시**

```nginx
server {
    listen 80;
    location / {
        proxy_pass http://backend-server:5000;
    }
}
```

- 사용자가 http://example.com/에 접속시 http://backend-server:5000으로 요청 전달



