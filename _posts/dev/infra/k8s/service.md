## Service



📍 pod의 문제점

- 쿠버네티스 개별의 클러스터의 네트워크를 가지고 있음
  - 외부와 통신을 위해 포트포워드, 서비스 등을 사용해왔음
- 일시적으로 생성한 컨테이너의 집합이기에 지속적으로 생성될 경우 서비스가 부적절함
  - IP의 지속적인 변동
  - 로드밸런싱 관리 필요
- 이러한 문제 해결을 위해 서비스 리소스가 존재
- pod의 IP가 변경될 때마다 재설정 하지 않도록 함



📍 서비스 생성 방법

- kubectl의 expose를 통해 생성하는 것이 가장 쉬움
- YAML을 통해 버전 관리 가능



📍 서비스

- pod를 선택해서 서비스가 가능한 형태로 만들어줌
- selector의 app을 선택해서 로드밸런싱 수행
- Type은 clusterIP 형태로 생성됨
  - 옵션을 통해 LoadBalancer로 만들 수 있음



📍 서비스 세션 고정하기

- 서비스가 다수의 포드로 구성되면 웹 서비스의 세션이 유지되지 않음
- 처음 들어왔던 ClientIP 그대로 유지하는 방법이 필요
- sessionAffinity: ClientIP 라는 옵션을 주어 해결



📍 다중 포트 서비스

- 포트에 나열해서 사용
- YAML 파일의 속성 중 s가 붙은 것들은 복수로 사용 가능
  - 구글, 네이버의 경우 80번 포트로 접근시 302 리다이렉션 코드 반환하여 443으로 다시 붙게함
  - 따라서 80과 443 둘다 열어놓음



📍 서비스 생성 실습

kubectl create deploy --image=gasbugs/http-go http-go --dry-run=client -o yaml > http-go-deploy.yaml

- deployment YAML 파일 생성

```yaml
apiVersion: v1
kind: Service
metadata:
  name: http-go-svc
spec:
  selector:
    app: http-go
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080

---

apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: http-go
  name: http-go
spec:
  replicas: 1
  selector:
    matchLabels:
      app: http-go
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: http-go
    spec:
      containers:
      - image: gasbugs/http-go
        name: http-go
        resources: {}
status: {}
```

- service 추가

kubectl get pod -o wide

- Pod에 해당하는 IP 확인

kubectl describe svc

- service에 해당하는 endpoint에 pod의 IP가 있는지 확인
- 레디네스 프로브같은 경우 준비가 되면 서비스로 등록되어 로드밸런싱이 될 것이라고 볼 수 있음

kubectl scale deploy http-go --replicas=5

kubectl get pod -w

kubectl describe svc

- replicas를 통해 복제 후 Endpoints 확인



📍 서비스 IP 고정 실습

kubectl edit svc http-go-svc

- 설정 변경

```yaml
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: "2024-03-05T04:26:23Z"
  name: http-go-svc
  namespace: default
  resourceVersion: "1196947"
  uid: 514aebba-776f-4c47-b21c-51a2fa299e3b
spec:
  clusterIP: 10.100.160.192
  clusterIPs:
  - 10.100.160.192
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: 8080
  selector:
    app: http-go
  sessionAffinity: ClientIP
  type: ClusterIP
status:
  loadBalancer: {}
```

kubectl edit configmap -n kube-system cilium-config

kube-proxy-replacement: strict

- session affinity가 ficilium의 기본 설정으로는 동작되지 않기에 위의 명령어 실행



















