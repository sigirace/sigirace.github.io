```yaml
version: '3.9'

services:
  # =================== MYSQL ===================
  mysql:
    image: mysql:8.0
    container_name: mysql-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: leeshin!
      MYSQL_USER: emun
      MYSQL_PASSWORD: leeshin!
      MYSQL_DATABASE: emun_db
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./backup/mysql:/backup
    networks:
      - emun-net

  # =================== MONGODB ===================
  mongo:
    image: mongo:6.0
    container_name: mongo-db
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: emun
      MONGO_INITDB_ROOT_PASSWORD: leeshin!
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
      - ./backup/mongo:/backup
    networks:
      - emun-net

  mongo-express:
    image: mongo-express:1.0.0-alpha.4
    container_name: mongo-express
    restart: always
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: emun
      ME_CONFIG_MONGODB_ADMINPASSWORD: leeshin!
      ME_CONFIG_MONGODB_SERVER: mongo-db
    ports:
      - "8081:8081"
    depends_on:
      - mongo
    networks:
      - emun-net

  # =================== MILVUS v2.3.3 ===================
  milvus-etcd:
    container_name: milvus-etcd
    image: quay.io/coreos/etcd:v3.5.5
    restart: always
    command:
      - etcd
      - --name=milvus-etcd
      - --data-dir=/etcd-data
      - --listen-peer-urls=http://0.0.0.0:2380
      - --initial-advertise-peer-urls=http://milvus-etcd:2380
      - --listen-client-urls=http://0.0.0.0:2379
      - --advertise-client-urls=http://milvus-etcd:2379
      - --initial-cluster=milvus-etcd=http://milvus-etcd:2380
    volumes:
      - milvus_etcd_data:/etcd-data
    networks:
      - emun-net

  milvus-minio:
    container_name: milvus-minio
    image: minio/minio:RELEASE.2023-06-23T20-26-00Z
    restart: always
    environment:
      MINIO_ROOT_USER: emun
      MINIO_ROOT_PASSWORD: leeshin!
    command: server /data --console-address ":9001"
    volumes:
      - milvus_minio_data:/data
    ports:
      - "9000:9000"
      - "9001:9001"
    networks:
      - emun-net

  milvus-standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.3.3
    restart: always
    command:
      - milvus
      - run
      - standalone
    environment:
      ETCD_ENDPOINTS: milvus-etcd:2379
      MINIO_ADDRESS: milvus-minio:9000
      MINIO_ROOT_USER: emun
      MINIO_ROOT_PASSWORD: leeshin!
    ports:
      - "19530:19530"  # gRPC
    volumes:
      - milvus_data:/var/lib/milvus
      - ./backup/milvus:/backup
    depends_on:
      - milvus-etcd
      - milvus-minio
    networks:
      - emun-net

  attu:
    container_name: attu
    image: zilliz/attu:v2.3.4
    restart: always
    environment:
      MILVUS_URL: milvus-standalone:19530
    ports:
      - "3000:3000"
    depends_on:
      - milvus-standalone
    networks:
      - emun-net

  # =================== OPENSEARCH ===================
  opensearch:
    image: opensearchproject/opensearch:2.10.0
    container_name: opensearch
    environment:
      - discovery.type=single-node
      - bootstrap.memory_lock=true
      - OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m
      - plugins.security.disabled=true  # 비밀번호 없이 실행 (테스트 용도)
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - opensearch_data:/usr/share/opensearch/data
    ports:
      - "9200:9200"
      - "9600:9600"
    networks:
      - emun-net

  opensearch-dashboards:
    image: opensearchproject/opensearch-dashboards:2.10.0
    container_name: opensearch-dashboards
    ports:
      - "5601:5601"
    environment:
      OPENSEARCH_HOSTS: '["http://opensearch:9200"]'
    depends_on:
      - opensearch
    networks:
      - emun-net

  # =================== FILE SERVER ===================
  filebrowser:
    image: filebrowser/filebrowser:s6
    container_name: filebrowser
    restart: always
    ports:
      - "8082:80"
    volumes:
      - ./filebrowser/data:/srv
      - ./filebrowser/config:/config
    environment:
      - FB_USER=emun
      - FB_PASSWORD=leeshin!
    networks:
      - emun-net

volumes:
  mysql_data:
  mongo_data:
  milvus_data:
  milvus_etcd_data:
  milvus_minio_data:
  opensearch_data:

networks:
  emun-net:
    driver: bridge
```



```
docker-compose -f docker-compose-db.yaml up -d
docker-compose -f docker-compose-db.yaml down
```

```
rm -rf docker-compose-db.yaml
vi docker-compose-db.yaml
```



```
sudo rm -rf ./filebrowser/config
sudo mkdir -p ./filebrowser/config


sudo rm -rf ./filebrowser/data
sudo mkdir -p ./filebrowser/data

docker logs --tail 50 filebrowser
docker logs --tail 50 milvus-standalone
```





```yaml
version: '3.9'

services:
  # =================== MYSQL ===================
  mysql:
    image: mysql:8.0
    container_name: mysql-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: leeshin!
      MYSQL_USER: emun
      MYSQL_PASSWORD: leeshin!
      MYSQL_DATABASE: emun_db
    ports:
      - "3306:3306"
    volumes:
      - /home/sigi/data/mysql:/var/lib/mysql
      - /home/sigi/data/backup/mysql:/backup
    networks:
      - emun-net

  # =================== MONGODB ===================
  mongo:
    image: mongo:6.0
    container_name: mongo-db
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: emun
      MONGO_INITDB_ROOT_PASSWORD: leeshin!
    ports:
      - "27017:27017"
    volumes:
      - /home/sigi/data/mongo:/data/db
      - /home/sigi/data/backup/mongo:/backup
    networks:
      - emun-net

  mongo-express:
    image: mongo-express:1.0.0-alpha.4
    container_name: mongo-express
    restart: always
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: emun
      ME_CONFIG_MONGODB_ADMINPASSWORD: leeshin!
      ME_CONFIG_MONGODB_SERVER: mongo-db
    ports:
      - "8081:8081"
    depends_on:
      - mongo
    networks:
      - emun-net

  # =================== MILVUS ===================
  milvus-etcd:
    image: quay.io/coreos/etcd:v3.5.5
    container_name: milvus-etcd
    restart: always
    command:
      - etcd
      - --name=milvus-etcd
      - --data-dir=/etcd-data
      - --listen-peer-urls=http://0.0.0.0:2380
      - --initial-advertise-peer-urls=http://milvus-etcd:2380
      - --listen-client-urls=http://0.0.0.0:2379
      - --advertise-client-urls=http://milvus-etcd:2379
      - --initial-cluster=milvus-etcd=http://milvus-etcd:2380
    volumes:
      - /home/sigi/data/milvus/etcd:/etcd-data
    networks:
      - emun-net

  milvus-minio:
    image: minio/minio:RELEASE.2023-06-23T20-26-00Z
    container_name: milvus-minio
    restart: always
    environment:
      MINIO_ROOT_USER: emun
      MINIO_ROOT_PASSWORD: leeshin!
    command: server /data --console-address ":9001"
    volumes:
      - /home/sigi/data/milvus/minio:/data
    ports:
      - "9000:9000"
      - "9001:9001"
    networks:
      - emun-net

  minio-mc:
    image: minio/mc
    container_name: minio-mc
    depends_on:
      - milvus-minio
    entrypoint: >
      /bin/sh -c "
      sleep 10 &&
      mc alias set local http://milvus-minio:9000 emun leeshin! &&
      mc mb -p local/a-bucket || echo 'Bucket already exists';
      exit 0;"
    networks:
      - emun-net

  milvus-standalone:
    image: milvusdb/milvus:v2.3.3
    container_name: milvus-standalone
    restart: always
    command:
      - milvus
      - run
      - standalone
    environment:
      ETCD_ENDPOINTS: milvus-etcd:2379
      MINIO_ADDRESS: milvus-minio:9000
      MINIO_ROOT_USER: emun
      MINIO_ROOT_PASSWORD: leeshin!
      COMMON_BLOB_STORAGE_BUCKET_NAME: a-bucket
    depends_on:
      - milvus-etcd
      - milvus-minio
      - minio-mc
    ports:
      - "19530:19530"
    volumes:
      - /home/sigi/data/milvus/milvus:/var/lib/milvus
      - /home/sigi/data/backup/milvus:/backup
    networks:
      - emun-net

  attu:
    image: zilliz/attu:v2.3.4
    container_name: attu
    restart: always
    environment:
      MILVUS_URL: milvus-standalone:19530
    depends_on:
      - milvus-standalone
    ports:
      - "3000:3000"
    networks:
      - emun-net

  # =================== OPENSEARCH ===================
  opensearch:
    image: opensearchproject/opensearch:2.10.0
    container_name: opensearch
    restart: always
    environment:
      - discovery.type=single-node
      - bootstrap.memory_lock=true
      - OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m
      - plugins.security.disabled=true
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - /home/sigi/data/opensearch:/usr/share/opensearch/data
    ports:
      - "9200:9200"
      - "9600:9600"
    networks:
      - emun-net

  opensearch-dashboards:
    image: opensearchproject/opensearch-dashboards:2.10.0
    container_name: opensearch-dashboards
    restart: always
    ports:
      - "5601:5601"
    environment:
      OPENSEARCH_HOSTS: '["http://opensearch:9200"]'
    depends_on:
      - opensearch
    networks:
      - emun-net

  # =================== FILE SERVER ===================
  filebrowser:
    image: filebrowser/filebrowser:s6
    container_name: filebrowser
    restart: always
    ports:
      - "8082:80"
    volumes:
      - /home/sigi/data/filebrowser/data:/srv
      - /home/sigi/data/filebrowser/config:/config
    entrypoint: >
      /bin/sh -c "
      if [ ! -f /config/filebrowser.db ]; then
        filebrowser --database /config/filebrowser.db config init &&
        filebrowser --database /config/filebrowser.db users add emun leeshin! --perm.admin &&
        filebrowser --database /config/filebrowser.db config set --branding.name 'e-mun Filebrowser' &&
        filebrowser --database /config/filebrowser.db config set --root /srv &&
        filebrowser --database /config/filebrowser.db config set --port 80 &&
        filebrowser --database /config/filebrowser.db config set --address 0.0.0.0;
      fi &&
      filebrowser --database /config/filebrowser.db"
    networks:
      - emun-net

# =================== NETWORK ===================
networks:
  emun-net:
    driver: bridge
```









```yaml
version: "3"
services:
  # Milvus 관련 서비스
  etcd:
    container_name: milvus-etcd
    image: quay.io/coreos/etcd:v3.5.5
    environment:
      - ETCD_AUTO_COMPACTION_MODE=revision
      - ETCD_AUTO_COMPACTION_RETENTION=1000
      - ETCD_QUOTA_BACKEND_BYTES=4294967296
      - ETCD_SNAPSHOT_COUNT=50000
    volumes:
      - /home/sigi/data/milvus/etcd:/etcd-data
    command: etcd -advertise-client-urls=http://127.0.0.1:2379 -listen-client-urls http://0.0.0.0:2379 --data-dir /etcd
    healthcheck:
      test: ["CMD", "etcdctl", "endpoint", "health"]
      interval: 30s
      timeout: 20s
      retries: 3

  minio:
    container_name: milvus-minio
    image: minio/minio:RELEASE.2023-03-20T20-16-18Z
    environment:
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
    ports:
      - "9001:9001"
      - "9000:9000"
    volumes:
      - /home/sigi/data/milvus/minio:/data
    command: minio server /minio_data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.4.6
    command: ["milvus", "run", "standalone"]
    security_opt:
      - seccomp:unconfined
    environment:
      ETCD_ENDPOINTS: milvus-etcd:2379
      MINIO_ADDRESS: milvus-minio:9000
    volumes:
      - /home/sigi/data/milvus/milvus:/var/lib/milvus
      - /home/sigi/data/backup/milvus:/backup
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9091/healthz"]
      interval: 30s
      start_period: 90s
      timeout: 20s
      retries: 3
    ports:
      - "19530:19530"

  attu:
    image: zilliz/attu:v2.3.4
    container_name: attu
    restart: always
    environment:
      MILVUS_URL: milvus-standalone:19530
    depends_on:
      - standalone
    ports:
      - "3000:3000"
      
networks:
  emun-net:
    external: true
```





```
sudo chown -R 1000:1000 /home/sigi/data/opensearch
```





```yaml
version: '3.8'

services:
  opensearch:
    image: opensearchproject/opensearch:2.14.0
    container_name: opensearch
    environment:
      cluster.name: opensearch-cluster
      node.name: opensearch-node
      discovery.type: single-node
      bootstrap.memory_lock: "true"
      OPENSEARCH_JAVA_OPTS: "-Xms512m -Xmx512m"
      OPENSEARCH_INITIAL_ADMIN_PASSWORD: "Leeshin93!"
      plugins.security.disabled: "true"  # 보안 비활성화 (운영환경에서는 false 권장)
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - /home/sigi/data/opensearch:/usr/share/opensearch/data
    ports:
      - "9200:9200"
      - "9600:9600"
    networks:
      - emun-net

  opensearch-dashboards:
    image: opensearchproject/opensearch-dashboards:2.14.0
    container_name: opensearch-dashboards
    environment:
      OPENSEARCH_HOSTS: '["http://opensearch:9200"]'
      OPENSEARCH_USERNAME: "admin"
      OPENSEARCH_PASSWORD: "Leeshin93!"
      DISABLE_SECURITY_DASHBOARDS_PLUGIN: "true"  # ✅ 보안 플러그인 미사용시 권장 옵션
    ports:
      - "5601:5601"
    depends_on:
      - opensearch
    networks:
      - emun-net

networks:
  emun-net:
    external: true
```



```
from fastapi import FastAPI, Depends, HTTPException, status, Query
import pymysql
import pymongo
from pymongo import MongoClient
from opensearchpy import OpenSearch
from pymilvus import connections, Collection, utility
import requests
from typing import Optional

# === FastAPI 앱 ===
app = FastAPI(
    title="E-MUN FastAPI + Key 인증",
    description="Key 인증 포함 MySQL, MongoDB, Milvus, Filebrowser, OpenSearch 테스트 서버",
    version="1.0.0"
)

# =======================================
# ✅ Key 인증 함수 (Depends로 적용)
# =======================================
API_KEY = "leeshin!"  # ✅ 고정 키값

def verify_api_key(key: Optional[str] = Query(None)):
    if key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="인증 실패: 유효하지 않은 키입니다."
        )
    return True

# =======================================
# ✅ 각 서비스 연결 설정 (로컬 기준)
# =======================================

# === MySQL 연결 정보 ===
MYSQL_HOST = "127.0.0.1"      # ✅ 로컬 MySQL
MYSQL_PORT = 3306
MYSQL_USER = "emun"
MYSQL_PASSWORD = "leeshin!"
MYSQL_DATABASE = "emun_db"

def get_db_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )

# === MongoDB 연결 정보 ===
MONGO_URI = "mongodb://127.0.0.1:27017"  # ✅ 로컬 MongoDB
MONGO_DB = "emun_db"

def get_mongo_client():
    return MongoClient(MONGO_URI)

# === Milvus 연결 정보 ===
MILVUS_HOST = "127.0.0.1"    # ✅ 로컬 Milvus
MILVUS_PORT = "19530"

def connect_milvus():
    connections.connect(
        alias="default",
        host=MILVUS_HOST,
        port=MILVUS_PORT
    )

# === Filebrowser 연결 정보 ===
FILEBROWSER_URL = "http://127.0.0.1:8082"  # ✅ 로컬 Filebrowser

# === OpenSearch 연결 정보 ===
OPENSEARCH_HOST = "127.0.0.1"  # ✅ 로컬 OpenSearch API
OPENSEARCH_PORT = 9200

def get_opensearch_client():
    return OpenSearch(
        hosts=[{'host': OPENSEARCH_HOST, 'port': OPENSEARCH_PORT}],
        http_auth=('admin', 'Leeshin93!'),
        use_ssl=False,
        verify_certs=False
    )

# =======================================
# ✅ 엔드포인트 (모두 API Key 보호)
# =======================================

@app.get("/echo")
def echo(auth=Depends(verify_api_key)):
    return {
        "message": "FastAPI + Key 인증 성공!"
    }

@app.get("/db-test")
def db_test(auth=Depends(verify_api_key)):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW() as now_time;")
            result = cursor.fetchone()
        conn.close()
        return {"db_time": result["now_time"]}
    except Exception as e:
        return {"error": str(e)}

@app.get("/mongo-test")
def mongo_test(auth=Depends(verify_api_key)):
    try:
        client = get_mongo_client()
        db = client[MONGO_DB]
        collections = db.list_collection_names()
        return {"mongo_collections": collections}
    except Exception as e:
        return {"error": str(e)}

@app.get("/milvus-test")
def milvus_test(auth=Depends(verify_api_key)):
    try:
        connect_milvus()
        collection_names = utility.list_collections()
        return {"milvus_collections": collection_names}
    except Exception as e:
        return {"error": str(e)}

@app.get("/filebrowser-test")
def filebrowser_test(auth=Depends(verify_api_key)):
    try:
        response = requests.get(FILEBROWSER_URL)
        return {"filebrowser_status_code": response.status_code}
    except Exception as e:
        return {"error": str(e)}

@app.get("/opensearch-test")
def opensearch_test(auth=Depends(verify_api_key)):
    try:
        client = get_opensearch_client()
        info = client.info()
        return {"opensearch_info": info}
    except Exception as e:
        return {"error": str(e)}

# =======================================
# 실행 명령어
# =======================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```







```
#!/bin/bash

# ✅ 클라우드플레어 터널링 스크립트
# 백그라운드 실행된 PID를 저장할 배열
PIDS=()

# 종료 시 모든 클라우드플레어 터널 종료
cleanup() {
  echo "🛑 Stopping all tunnels..."
  for pid in "${PIDS[@]}"; do
    kill "$pid"
  done
  echo "✅ All tunnels stopped."
  exit 0
}

# SIGINT(Ctrl+C), SIGTERM 시 종료 트랩
trap cleanup SIGINT SIGTERM

# ✅ TCP 터널 명령 실행 함수
run_tcp_tunnel() {
  local service_name=$1
  local hostname=$2
  local local_url=$3

  echo "🚀 Starting TCP tunnel for ${service_name} (${hostname} -> ${local_url}) ..."
  cloudflared access tcp --hostname "${hostname}" --url "${local_url}" &
  pid=$ㅈㅂ!
  PIDS+=($pid)
  sleep 1
}

# ✅ HTTP 터널 명령 실행 함수 (임시 HTTP 터널)
run_http_tunnel() {
  local service_name=$1
  local hostname=$2
  local local_url=$3

  echo "🚀 Starting HTTP tunnel for ${service_name} (${hostname} -> ${local_url}) ..."
  cloudflared tunnel --url "${local_url}" --hostname "${hostname}" &
  pid=$!
  PIDS+=($pid)
  sleep 1
}

# ✅ TCP 서비스 (데이터베이스, Milvus)
run_tcp_tunnel "MySQL" "mysql.e-mun.com" "localhost:3306"
run_tcp_tunnel "MongoDB" "mongo.e-mun.com" "localhost:27017"
run_tcp_tunnel "Milvus" "milvus.e-mun.com" "localhost:19530"

# ✅ HTTP 서비스 (Filebrowser, OpenSearch API)
run_http_tunnel "Filebrowser" "filebrowser.e-mun.com" "http://localhost:8082"
run_http_tunnel "OpenSearch API" "opensearch-api.e-mun.com" "http://localhost:9200"

echo "✅ All tunnels started!"
echo "👉 Use 'ps aux | grep cloudflared' to check running tunnels."

# 무한 대기 → 터널이 살아있도록
while true; do
  sleep 10
done
```



```
sudo pkill cloudflared
```

