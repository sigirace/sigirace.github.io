[저장소 업데이트]

sudo apt update

[도커 설치]

sudo apt install docker.io -y



[도커 권한 수정]

﻿sudo usermod -aG docker $USER && newgrp docker



[minikube 다운로드 및 설치]

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

sudo dpkg -i minikube_latest_amd64.deb



[실행]

minikube start --driver=docker



[kubectl 설치]

sudo snap install kubectl --classic



[노드 조회 명령 수행]

kubectl get nodes



docker ps

- 1개의 컨테이너가 보임
- 큰 클러스터가 미니큐브라는 노드가 도커에 할당되어 있음
- 사용하는 다양한 포트들을 밖으로 포트포워딩 해 주고 있음



[SSH 접속]

minikube ssh

- 도커 컨테이너 진입
- 컨테이너 안에 도커가 있고 클러스터를 구성하는 컨테이너들이 나옴
- 실제 쿠버네티스와는 다소 차이점이 있음



[애플리케이션 배포]

[파드확인]

kubectl get pod

[배포]

kubectl create deploy hello-minikube --image=k8s.gcr.io/echoserver:1.10

- 간단한 에코 서버

kubectl expose deploy hello-minikube --type=NodePort --port=8080

- 외부로 에코서버에 대한 정보 노출

kubectl get svc

- 헬로우 미니큐브가 노드포트라는 이름으로 포트를 열고 있는 것을 볼 수 있음
- 자세한 설명은 나중에

cat .kube/config

- server의 주소 가져옴 -> 노드의 정보
- 8443: API 서비스 (kubectl을 통해 접속하는 포트)

curl server_ip:port



