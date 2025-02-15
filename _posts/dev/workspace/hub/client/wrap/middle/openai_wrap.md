## 🕸️ Constants

```
OPENAI = "openai"
```



## 🎹 _OpenAI

### 📍 상속

- LlmHub
  - 설명: client > base > base.md

### 📍 `__init__`

- parameters
  - service
    - default: OPENAI
  - user
  - session
  - req_id
  - user_ip
  - plugin_name
  - filters
  - disable_audit
  - ai_hub_url
  - group_key

```python
  def __init__(self, service: str = OPENAI, user: str = None, session: str = None, req_id: str = None,
               user_ip: str = None, plugin_name: str = None, filters: str = None, disable_audit: bool = False, 
               ai_hub_url: str = None, group_key: str = None, time_offset: int = 0):
      super().__init__(service, user, session, req_id, user_ip, plugin_name, 
                       filters, disable_audit, ai_hub_url, group_key, time_offset)
      self.headers = None
```

- LlmHub 초기화: Router로 보내기 위한 정보 세팅

### 📍 `_create`

- classmethod
- 







