kubernetes 공식문서 : https://kubernetes.io/ko/



- master: ssh sigi@192.168.243.131
- worker1: ssh sigi@192.168.243.132
- worker2: ssh sigi@192.168.243.130





umedy: https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/?couponCode=ACCAGE0923





📒 **http-go-deploy.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: http-go-svc
spec:
  selector:
    run: http-go
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
      - image: sigirace/http-go:v1
        name: http-go
        resources: {}
status: {}
```

📒 **http-go-np.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: http-go-np
spec:
  type: NodePort
  selector:
    run: http-go
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
      nodePort: 30001
```

