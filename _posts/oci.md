## key 파일 권한 및 접속

```
chmod 600 [.key_path]
ssh -i [.key_path] ubuntu@[public_ip]
```

## OCI 권한 설정

```
sudo usermod -aG [명령어] $[user_name]
```

## Ubuntu Docker 설치

- version: 22.04

```
1. 우분투 시스템 패키지 업데이트
sudo apt-get update
2. 필요한 패키지 설치
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
 

3. Docker의 공식 GPG키를 추가
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
 

4. Docker의 공식 apt 저장소를 추가
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
 

5. 시스템 패키지 업데이트
sudo apt-get update
6. Docker 설치
sudo apt-get install docker-ce docker-ce-cli containerd.io
 

7. Docker가 설치 확인
7-1 도커 실행상태 확인
sudo systemctl status docker
7-2 도커 실행
sudo docker run hello-world

# Docker compose install
sudo apt install -y docker-compose
```

## Docker mysql 설치

```
docker pull mysql


# docker-compose.yaml
version: "3" # 파일 규격 버전
services: # 이 항목 밑에 실행하려는 컨테이너 들을 정의
  mysql: # 서비스 명
    image: mysql:latest # 사용할 이미지
    container_name: mysql # 컨테이너 이름 설정
    ports:
      - "3306:3306" # 접근 포트 설정 (컨테이너 외부:컨테이너 내부)
    restart: always
    environment: # -e 옵션
      MYSQL_ROOT_PASSWORD: "PASSWORD"  # MYSQL 패스워드 설정 옵션
      TZ: "Asia/Seoul"
    command: # 명령어 실행
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
    volumes:
      - /app/volume/mysql:/var/lib/mysql # -v 옵션 (다렉토리 마운트 설정)
      

# up
docker-compose -f docker-compose-mysql.yaml up -d

# exec
docker exec -it mysql mysql -u root -p
```

## OCI 접속설정

```
# 먼저 root의 비밀번호 설정을 한다.
sudo passwd root
# 그리고 ubuntu 계정의 비밀번호 설정도 해준다.
sudo passwd ubuntu

# 개인키 없이 원격 접속 허용
# cd /etc/ssh
# sshd 설정 파일을 건드리기 전에 백업본을 만들어둔다.
sudo cp sshd_config sshd_config.bak

# sshd 설정 파일을 수정한다.
sudo nano sshd_config

# PasswordAuthentication을 yes로 바꾸고 저장
# ctrl+o, Enter, ctrl+x

# 저장하고 나서는 ssh를 재실행해준다.
sudo service sshd reload

# 재접속
ssh ubuntu@공공 IP
# 잘안되네;
```

## OCI Mysql

```
# 오라클 인스턴스 > 서브넷 > 보안 목록 항목 클릭 > 수신 규칙 추가 > 소스 CIDR: 0.0.0.0/0, 대상포트범위 3306, 설명 MySQL

# 방화벽 사용 중지
sudo iptables -F

# 방화벽 작동 목록 확인
sudo iptables -L

# 방화벽 정책 영속화 패키지 설치
sudo apt install -y iptables-persistent netfilter-persistent net-tools

# 영속화
sudo netfilter-persistent save

# 외부 접속
mysql -h [public_ip] -u root -p
```

## Mongo

```
docker pull mongo

# docker-compose-mongo.yaml

version: '3.8'
services:
  mongodb:
    image: mongo
    container_name: mongodb
    restart: always
    ports:
      - 27017:27017
    volumes:
      - ~/mongodb:/data/db
    environment:
      - MONGO_INITDB_ROOT_USERNAME=root
      - MONGO_INITDB_ROOT_PASSWORD=sigirace!

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: sigirace!
      ME_CONFIG_MONGODB_URL: mongodb://root:sigirace!@mongodb:27017
```



**DBeaver**

- https://velog.io/@dailylifecoding/DBeaver-MySQL-connecting-error-Public-Key-Retrieval-is-not-allowed-solved

**Telnet**

- https://stackoverflow.com/questions/54794217/opening-port-80-on-oracle-cloud-infrastructure-compute-node







### docker image ls

-> 이미지 리스트

### docker ps -a

-> 컨테이너 리스트 (process)

### docker run -d --rm --name mycontainer -p 8080:80 ngninx

`-d`: 백그라운드 실행

`-rm`: 컨테이너 내리면 삭제함

### docker exec -it mycontainer bash

-> bash로 실행시키려면 -it을 통해 터미널을 붙여야 함

-> bash로 nginx를 실행하여 ls를 확인하면 리눅스 구조랑 동일

-> 리눅스에서 nginx 실행한 것

### docker conatiner export [container_name] > [export_name]

`>`는 리눅스 출력 전환 기호

### docker image import [export_name] [image_name]

### docker exec -it mycontainer bash

-> 진입

-> nginx는 entrypoint가 존재함

### docker image save -o [new_image_name] [org_img_name]

`-o`: output하라는 명령어

### docker image load -i mysave.img

-> 내가 가진 현재 이미지에 동일하게 풀림

### ADD [source] [destination]

-> ADD 명령어는 source를 destination으로 복사

### docker tag [image_name] [계졍]/[repository]:[tag]

### docker push [계졍]/[repository]:[tag]

### docker image pull [계졍]/[repository]:[tag]

### docker run -d --restart=always -p 5000:5000 --name myregistry registry

## Network

### sudo ip net add [namespace]

### sudo ip netns [namespace] ip link

### sudo ip link add veth-[namespace] type veth peer name veth-[peer namespace]

-> 가상 이더넷 안에는 라우팅 테이블과 arp 테이블이 존재

### sudo ip link set veth-[namespace] netns [namespace]

### sudo ip -n red addr add 192.168.15.1/24 dev veth-red

-> 어댑터에 ip address 할당

### sudo ip -n red link set veth-red up

-> run

### docker network inspect bridge

chmod u+x *.sh

./container-ip.sh

mkdir ~.bin

su - [user] -> login

contianer-ip.sh

### docker network create [network_name]

-> default: bridge

### docker network connect [brdige_ name] [container_name]

-> container에 다른 bridge와 통신하기 위한 새로운 Ip가 할당됨
