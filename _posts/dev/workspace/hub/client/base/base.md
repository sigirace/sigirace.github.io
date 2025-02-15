## 🎹 LlmHub

> HONE-AIHUB-GO의 Router로 요청을 보내는 부분

### 📍 Initialize

- `ai_service`
- `ai_hub_url`
  - _check_ai_hub_url
- `plugin_name`
  - _check_plugin_name 
- `url`: None
- `user`: parameter
- `req_id`
- `session`
- `user_ip`
- `filters`
- `disable_audit`
- `time_offset`
- `group_key`
  - _check_group_key

### 📍 get_url

- params: `service_type`, `service_path`
- 👉 self.ai_hub_url + svc_type + "/" + self.ai_service + service_path

### 📍 request

- params: `svc_type`, `service_path`, `payload_obj`, `extra_headers:dict`, `stream:bool`
- time_offset 설정
  - 0
- group_key 설정
  -  "HaiGroupKey " + self.group_key
-  headeer 설정

```python
headers = {
            "Authorization": self.group_key,
            "H-Plugin-Name": self.plugin_name,
            "H-User": self.user,
            "H-Session": self.session,
            "H-Req-Id": self.req_id,
            "H-User-Ip": self.user_ip,
            "H-Tm-Offset": str(self.time_offset),
        }
```

- extra_headers 설정
- url 설정
  - 📍 get_url: self.ai_hub_url + svc_type + "/" + self.ai_service + service_path
- ai_service (private, clova 등)에 따라 json parsing
- request post
  - url
  - json : 데이터







### ⚙️ Functions

🔗 **_check_ai_hub_url**

- case1: aihub package에 등록됨
- case2: os.getenv(ENV_AI_HUB_URL)
  - "http://localhost:6661/v2/route/"

🔗 **_check_plugin_name**

- case1: aihub package에 등록됨
- case2: os.getenv(ENV_PLUGIN_NAME)
  - "test-app"

🔗 **_check_group_key**

- case1: aihub package에 등록됨
- case2: os.getenv(ENV_GROUP_KEY)
  - "hai-607cd575125bbf410a368244861ee8e9"







 