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
