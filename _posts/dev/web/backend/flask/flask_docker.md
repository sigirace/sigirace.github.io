## 1. 파일

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

```
docker run --platform linux/amd64 -d -p 5005:5000 -p 3030:3030 --name flask --network test ubuntu:22.04 tail -f /dev/null
```

```
docker run --platform linux/amd64 -d -p 81:80 --name nginx --network test ubuntu:22.04 tail -f /dev/null
```
