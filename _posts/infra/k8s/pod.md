[pod]

- 쿠버네티스는 컨테이너를 개별적으로 배포하지 않고 컨테이너의 포드를 배포 및 운영
- 일반적으로 포드는 단일 컨테이너만 포함하지만 다수의 컨테이너 포함 가능
  - 스케일링을 위해 단일 컨테이너를 권장
  - 두가지의 컨테이너가 밀접한 관계일 경우에만 한 포드에 넣음

- 여러 노드에 걸쳐서 생성되지 않고 단일 노드에서만 생성 및 실행
- 다수 컨테이너일 경우 컨테이너간 자원 공유 가능

📍 장점

- 연관된 프로세스를 하나의 환경에서 동작하는 것처럼 함께 실행
- 그러나 다소 격리된 상태로 유지



📍 네트워크 구조

- pod이 할당받은 네트워크 대역대에서 순차적으로 증가하는 형태
- 서로간의 통신도 잘 됨
- NAT 게이트웨이가 따로 존재하지 않음
- 외부에서 해당 IP로 접근하는 것은 불가능하며 외부에 서비스 객체 생성해야함



📍 파드 구성요소

- apiVersion: 쿠버네티스의 api 가 일치해야 통신 가능 일종의 프로토콜
- kind: 리소스의 유형 결정 (pod, replica, service ...)
- 메타데이터: apiversion과 kind를 만들 때, 어떤 식으로 데이터를 생성할 것인지 정의
- 스펙: 어떤 컨테이너를 배치하고 볼륨을 설정하고 등등 자세한 정보
- 스테이터스: 포드의 일반적인 상태 외에 기본정보 같은 것이 들어가 있음, 쿠버네티스가 해주는 것



📍 쿠버네티스 리소스 종류

- **Pod (파드)**: 쿠버네티스 애플리케이션의 기본적인 빌딩 블록으로, 하나 이상의 컨테이너가 포함된 그룹입니다. 파드는 스케일링, 네트워킹, 스토리지 리소스를 공유합니다.
- **Service (서비스)**: 파드 집합에 대한 안정적인 네트워크 주소를 제공합니다. 서비스는 파드에 도달하기 위한 내부 네트워크에서의 고정 IP 주소와 포트를 정의하며, 로드 밸런싱을 제공합니다.
- **ReplicaSet (레플리카셋)**: 지정된 수의 파드 복제본이 항상 실행되도록 보장합니다. ReplicaSet은 파드의 스케일링과 장애 복구를 관리합니다.
- **Deployment (디플로이먼트)**: 파드와 ReplicaSet의 선언적 업데이트를 제공합니다. 디플로이먼트를 사용하면 애플리케이션의 배포, 롤백, 업데이트를 쉽게 관리할 수 있습니다.



[pod 실습]

cd ~

mkdir yaml

cd yaml

vi go-http-pod.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: http-go
  labels:
    app: http-go
spec:
  containers:
  - name: http-go
    image: gasbugs/http-go
    ports:
    - containerPort: 8080
```

kubectl create -f go-http-pod.yaml

- 파일에 정의된 내용을 기반으로 쿠버네티스 리소스를 생성

kubectl get pod http-go

kubectl get pod http-go -o wide

- 생성 확인

kubectl annotate pod http-go test1234=test1234

- 주석생성

kubectl delete -f go-http-pod.yaml

- 삭제

kubectl delete pod --all

- 모두삭제



[Probes]

- 각각의 기능들이 포드를 보조하는 역할을 수행
- 포드 내부에 설정파일로 존재

📍 Liveness Probe

- 살아있는지 판단하고 살아있지 않다면 다시 시작 ☞ 가용성

📍 Readiness Probe

- 포드가 준비된 상태에 있는지 확인하고 정상 서비스를 시작
- 포드가 준비되지 않은 경우 로드밸런싱을 하지 않음
  - 서비스가 포드로 로드밸런싱을 할텐데 레디니스 체크 후 로드밸런싱 리스트 생성

📍 Startup Probe

- 애플리케이션 시작 시기를 확이냏서 가용성을 높임
- Liveness와 Readiness를 비활성화하고 컨테이너가 시작할 수 있는 시간을 벌어줌

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/



[레이블과 셀렉터]

- 모든 서비스에 레이블과 셀렉터 없이는 돌아가 ㄹ수 없음

📍 레이블

- 리소스를 인식하기 위한 바코드 역할
- 리소스의 목적에 따라 검색을 수행할 수 있게 됨
  - 다수의 레이블을 가질 수 있음
  - 만드는 시점에 레이블을 첨부하나 수정, 추가 가능
- 리소스에 키/값 쌍으로 첨부하여 사용 ex) app:test
- 체계적인 시스템 구축
  - app: 애플리케이션 구성요소, 마이크로서비스 유형 지정
  - rel: 애플리케이션 버전 지정 (release, 버전)



📍 포드 생성 시 레이블 지정

- metadata의 labels에 지정 > 여러개 가능

```
metadata:
	name: app_name
	labels:
		key1: value1
		key2: value2
```



📍 명령어

kubectl label pod [name] [key]=[value]

- 레이블을 추가 및 수정

kubectl label pod [name] [key]=[value] --overite

- 기존 레이블 수정

kubectl label pod [name] [key]-

- 레이블 삭제

kubectl get pod --show-lables

- 레이블 확인

kubectl get pod -L [key1],[key2]

- 특정 레이블 컬럼으로 확인

kubectl get pod --show-lables -l ['key']

kubectl get pod --show-lables -l ['key' = or != 'value']

- 필터링하여 검색



📍 레이블 배치 전략

https://cast.ai/blog/kubernetes-labels-expert-guide-with-10-best-practices/



[Replication Controller]

📍 Replication Controller

- replicaset의 구버전 (v1.8 이전)
- 포드가 잘 생성되었는지 감시하고, 장애가 났다면 재생성
- 지속적으로 모니터링하고 실제 포드수가 원하는 포드수와 맞는지 체크



📍 레플리케이션 컨트롤러 세가지 요소

- 레이블 셀렉터: 포드의 범위를 결정
- 복제본 수: 포드의 수를 결정
- 포드 템플릿: 새로운 포드의 모양을 설명, 레플리카셋 하위에 포드가 생성되기 위한 포드의 정보



📍 레플리케이션 컨트롤러의 장점

- 포드가 없는 경우 새 포드를 실행
- 노드 장애 발생시 다른 노드에 복제본 생성
- 수동, 자동으로 수평 스케일링



📍 레플리케이션 컨트롤러 실습

```yaml
# replication.yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

- pod의 템플릿이 가지고 있는 label과 셀렉터 부분의 label이 동일해야함



kubectl create -f replication.yaml

- replication controller 생성

kubectl get pod

- 생성 확인

kubectl delete pod nginx-2wc9b

kubectl get pod

- 삭제 후 rc에 의해 신규 파드 생성 확인

kubectl label pod nginx-85vgc app-

kubectl get pod

- 라벨 삭제 및 rc에 의해 신규 파드 생성 확인

kubectl get pod -o wide

- Node 확인

kubectl get nodes -w

- worker2 정지
- 노드의 상태가 Ready로 변경

kubectl get pod -w

- 5분 후에 변경사항 반영됨
- 컨테이너를 빠르게 반응하면 자원 문제가 발생할 수 있기에 시간 텀을 둠
- 5분 뒤에 terminating > pending 상태를 거쳐 worker1에 생성됨

kubectl get nodes -w

- worker2 시작
- worker2가 ready로 변경

kubectl get pod -o wide

- 장애가 났을때 만들어졌던 파드들은 삭제됨
- 쿠버네티스 자체 리소스가 충분하기에 worker1에만 배치됨
  - 리소스가 부족하면 분산배치함



📍 레플리케이션 수정

✏️ 명령어

kubectl scale rc [name] --replicas=[num]

kubectl edit rc [name]



✏️ 복사후 configure

cp [old_yaml] [new_yaml]

kubectl apply -f [new_yaml]



📍 레플리케이션 삭제

kubectl delete rc [name]



[ReplicaSet]

- 레플리케이션 컨트롤러와 거의 동일하게 동작
- 레플리케이션 컨트롤러는 레이블을 유연하게 선택하기 어려운 단점이 있음
- 레플리카셋은 이를 극복



📍 레플리카셋 생성 및 명령어

- matchExpression을 통해 다양한 표현 생성

kubectl get rs

kubectl describe rs [name]

kubectl delete rs [name]



[Deployment]

- 배포를 위한 리소스
- 레플리카셋을 다룰 수 있는 객체
  - 다수의 레플리카 셋을 컨트롤 할 수 있음
- 레플리카셋의 업데이트를 좀 더 원활하게 도와줌



📍 포드 업데이트 방법

- recreate: 잠깐의 다운 타임 발생, 포드가 삭제되고 올라옴
- rolling update: 포드 여러개 중에 낮은 버전을 삭제하고 높은 버전을 하나씩 교체하며 올림



📍 디플로이먼트 스케일링

kubectl edit deploy [name]

kubectl scale deploy [name] --replicas=[num]



📍 연습문제-jenkins 배포

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-jenkins
  labels:
    app: jenkins-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: jenkins-test
  template:
    metadata:
      labels:
        app: jenkins-test
    spec:
      containers:
      - name: jenkins
        image: jenkins/jenkins
        ports:
        - containerPort: 8080
```

kubectl get all

- deployment > replicates > pod 순으로 랜덤 스트링이 뒤에 붙음을 알 수 있음

kubectl delete pod [pod_name]

kubectl describe rs [replicaset_name]

- 삭제, 생성에 대한 내용 확인



📍 롤링 업데이트 전략 세부 설정

- maxSurge
  - 최대 몇개까지의 pod를 배포할 수 있게 할 것이냐
  - 기본값은 25% ex) 10개 생성시 2~3 더 만들어짐
- maxUnavailable
  - 최소 몇개의 pod를 유지할 것인가
  - 기본값은 25% ex) 10개 생성시 7~8개는 유지됨

- 값이 클 수록 빠르게 배포될 수 있으나 자원 문제가 있을 수 있음



✏️ 배포 명령어

kubectl create -f http-go-deployment.yaml --record=true

- record를 통해 history에 명령어를 기록

kubectl rollout history deployment [name]

- history가 최대 10개까지 저장 ☞ 레플리카셋이 10개까지 가능

kubectl patch deployment [name] -p '{"spec": {"mainReadySeconds": [sec]}}'

- 업데이트 속도 조절

kubectl rollout pause deployment [name]

- 업데이트 중에 일시정지

kubectl rollout undo deployment [name]

- 업데이트 일시중지 중 취소

kubectl rollout resume deployment [name]

- 업데이트 재시작



📍 롤링 업데이트 실습

```yaml
# http-go-deploy-v1.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: http-go
  labels:
    app: http-go
spec:
  replicas: 3
  selector:
    matchLabels:
      app: http-go
  template:
    metadata:
      labels:
        app: http-go
    spec:
      containers:
      - name: http-go
        image: gasbugs/http-go:v1
        ports:
        - containerPort: 8080
```

kubectl create -f http-go-deploy-v1.yaml --record=true

- 배포

kubectl rollout status deploy http-go

- 상태 확인

kubectl rollout history deploy http-go

- history 확인

kubectl patch deploy http-go -p '{"spec":{"minReadySeconds":10}}'

- 10초 간격으로 업데이트 수행
- 모니터링을 위한 명령어

kubectl expose deploy http-go

- 로드밸런싱을 위한 서비스 생성

kubectl get svc

- 서비스 ip 확인

kubectl run -it --rm --image busybox -- bash

- busybox라는 이미지로 bash를 실행시킴 like docker

while true; do wget -O- -q 10.106.1.87:8080; sleep 1; done

- 쉘스크립트
- 신규 터미널 생성

kubectl set image deploy [deployment_name] [container_name]=[new_image] --record=true

- 업데이트 수행

kubectl rollout history deploy [deployment_name]

- history 확인 가능
- replicaset의 내용이 바뀌지 않으면 덮어씌워짐

kubectl rollout undo deploy http-go

- 이전 버전으로 rollback

kubectl rollout undo deploy http-go --to-revision=1

- 특정 revision으로 변경



[Namespaces]













