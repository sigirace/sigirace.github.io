## 📒 nginx.conf.template

```nginx
events {
    # configuration of connection processing
    worker_connections 2048;
}

http{

    upstream routers {
        least_conn;
        #SERVERS#
    }

    upstream files {
        least_conn;
        #FILE_SVCS#
    }

    server {
      listen       80;
      server_name  grima;

      proxy_http_version 1.1;

      location /v1/route {
        proxy_pass  http://routers;
        proxy_set_header Host $host;
    	proxy_set_header X-Real-IP $remote_addr;
      	proxy_buffer_size          128k;
      	proxy_buffers              4 256k;
      	proxy_busy_buffers_size    256k;
      	proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
        send_timeout 300;
      }

      location /v2/route {
        proxy_pass  http://routers;
        proxy_set_header Host $host;
    	proxy_set_header X-Real-IP $remote_addr;
      	proxy_buffer_size          128k;
      	proxy_buffers              4 256k;
      	proxy_busy_buffers_size    256k;
      	proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
        send_timeout 300;
      }

      location /v1/fs {
        proxy_pass  http://files;
        proxy_set_header Host $host;
    	proxy_set_header X-Real-IP $remote_addr;
      	proxy_buffer_size          128k;
      	proxy_buffers              4 256k;
      	proxy_busy_buffers_size    256k;
      	proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
        send_timeout 300;
      }
    }
}


```

- 이 nginx.conf.template는 **NGINX 리버스 프록시(Reverse Proxy) 및 로드 밸런싱**을 설정하는 템플릿입니다.
- 스크립트에서 #SERVERS#와 #FILE_SVCS#를 실제 서버 리스트로 대체하여 최종 nginx.conf를 생성합니다.

**✅ upstream 블록 (로드 밸런싱)**

- upstream routers {} → /v1/route, /v2/route 요청을 처리할 **백엔드 서버 그룹**
- upstream files {} → /v1/fs 요청을 처리할 **파일 서비스 서버 그룹**
- least_conn; → **가장 적은 연결을 가진 서버에 요청을 전달** (Least Connections Load Balancing)
- #SERVERS# 및 #FILE_SVCS# → **스크립트에서 실제 서버 리스트로 치환됨**

**📍 server 블록 (프록시 설정)**

```nginx
server {
  listen       80;
  server_name  grima;
```

- **NGINX가 80번 포트에서 HTTP 요청을 수신**
- server_name grima; → 도메인 네임 또는 호스트 이름 (grima 서버에서만 응답)



## 📒 set_nginx.conf.sh

**🔍 스크립트 해석 (nginx.conf 파일 생성 스크립트)**

이 Bash 스크립트는 **NGINX 설정 파일(nginx.conf)을 생성**하는 역할을 합니다.

**1️⃣ HOST_IP 변수 설정**

```
export HOST_IP=$(./host_ip.sh)
```

- HOST_IP 변수에 ./host_ip.sh 스크립트 실행 결과(서버의 IP 주소)를 저장.
- 즉, host_ip.sh가 실행되면 해당 머신의 IP를 반환하고, 그 값을 HOST_IP에 할당.

**2️⃣ 기존 nginx.conf.temp 및 nginx.conf 삭제**

```
rm nginx.conf.temp
rm nginx.conf
```

- 기존 nginx.conf.temp와 nginx.conf 파일을 삭제하여 새로운 설정을 생성하기 전 초기화.

**3️⃣ servers 변수 생성 (포트 6661~6671)**

```
servers=""

port_from=6661
port_to=6671

for (( i=$port_from; i<=$port_to; i++ ))
do
  servers+="        server ${HOST_IP}:$i;\n"
done
```

- servers 문자열 변수에 **6661~6671 포트 범위의 서버 리스트를 추가**.
- 예를 들어, HOST_IP가 192.168.1.100이라면 아래와 같은 문자열이 생성됨:

```
      server 192.168.1.100:6661;
      server 192.168.1.100:6662;
      server 192.168.1.100:6663;
      ...
      server 192.168.1.100:6671;
```

- \n은 줄바꿈 문자이지만, Bash에서 제대로 동작하려면 **echo -e 옵션을 사용**해야 함.

**4️⃣ #SERVERS#를 servers 값으로 치환**

```
sed "s/        #SERVERS#/$servers/g" ./nginx.conf.template > nginx.conf.temp
```

- nginx.conf.template 파일에서 #SERVERS#를 servers 문자열로 치환하여 nginx.conf.temp 파일을 생성.
- 즉, nginx.conf.template에서 아래와 같은 부분이 있을 때:

```
upstream backend {
      #SERVERS#
}
```

→ 이 부분이 실제 서버 리스트(servers)로 바뀜.

**5️⃣ fs_servers 변수 생성 (포트 9561~9571)**

```
fs_servers=""

port_from2=9561
port_to2=9571

for (( i=$port_from2; i<=$port_to2; i++ ))
do
  fs_servers+="        server ${HOST_IP}:$i;\n"
done
```

- fs_servers 문자열 변수에 **9561~9571 포트 범위의 서버 리스트를 추가**.
- HOST_IP가 192.168.1.100이라면 아래와 같은 내용이 생성됨:

```
      server 192.168.1.100:9561;
      server 192.168.1.100:9562;
      server 192.168.1.100:9563;
      ...
      server 192.168.1.100:9571;
```

**6️⃣ #FILE_SVCS#를 fs_servers 값으로 치환**

```
sed "s/        #FILE_SVCS#/$fs_servers/g" ./nginx.conf.temp > nginx.conf
```

- nginx.conf.temp 파일에서 #FILE_SVCS#를 fs_servers 값으로 치환하여 최종 nginx.conf 파일을 생성.
- nginx.conf.template에서 다음과 같은 부분이 있다면:

```
upstream file_services {
      #FILE_SVCS#
}
```

→ 실제 서버 리스트(fs_servers)로 바뀜.

**📌 최종 결과 (nginx.conf)**

최종적으로 생성되는 nginx.conf 파일은 대략 다음과 같은 내용이 됩니다.

```
upstream routers {
        server 192.168.1.100:6661;
        server 192.168.1.100:6662;
        server 192.168.1.100:6663;
        ...
        server 192.168.1.100:6671;
}

upstream files {
        server 192.168.1.100:9561;
        server 192.168.1.100:9562;
        server 192.168.1.100:9563;
        ...
        server 192.168.1.100:9571;
}
```

**🚀 결론 (스크립트 요약)**

	1. host_ip.sh 실행 → 서버 IP(HOST_IP) 저장.
	1. 기존 nginx.conf 및 nginx.conf.temp 삭제.
	1. **포트 6661~6671**에 대해 servers 리스트 생성.
	1. **포트 9561~9571**에 대해 fs_servers 리스트 생성.
	1. nginx.conf.template에서 #SERVERS#와 #FILE_SVCS#를 실제 서버 목록으로 치환.
	1. 최종적으로 nginx.conf를 생성.

이 스크립트는 **NGINX의 upstream 블록을 자동으로 생성하여 로드 밸런싱을 설정**하는 역할을 합니다. 🚀