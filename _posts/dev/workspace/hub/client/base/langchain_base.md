## 🎹 AiHubLLM

> langchain 패키지의 LLM 클래스를 상속받아 기능을 사용하기 위함

```python
from abc import ABC
from typing import Optional
from langchain.llms.base import LLM


class AiHubLLM(LLM, ABC):
    ai_hub_url: str = None
    model: Optional[str] = None
    base_model: Optional[str] = None
    max_tokens: int = 4000
    top_p: int = 1
    temperature: float = 0.3
    user: str = None
    user_ip: str = None
    req_id: str = None
    session_id: str = None
    group_key: str = None
    plugin_name: str = None
    api_version: str = None
    service: str = None
    time_offset: int = 0
    disable_audit: bool = False

    @property
    def _llm_type(self) -> str:
        return "aihub"
```

**📌 `ABC` 사용 이유**

> - 현재 `@abstractmethod`는 없지만, 향후 추가될 가능성을 고려하여 추상 클래스로 설계됨.
> - 직접 사용되지 않고 하위 클래스에서 확장하는 용도로 유지됨.

**📌 `AiHubLLM`을 만든 이유**

> - LangChain의 `LLM`을 상속하여 **AI Hub API에 필요한 속성을 추가**하고, **Langchain의 기능들을 사용**하기 위함
>   - `_call`, `_generate` 등의 method를 wrap한 클래스에서 사용가능
>   - `_call`은 오버라이드를 통해 내부에서 LlmHub를 타도록 수행
> - `_llm_type`을 통해 LangChain 내부에서 "aihub" 모델로 구별 가능.

**📌 `ABC`를 유지하는 이유**

> - `AiHubLLM`은 직접 사용되지 않고 확장하도록 설계됨.
> - "이 클래스를 직접 사용하지 말고 상속해서 써야 한다"는 의미를 명확히 전달.
> - 향후 `@abstractmethod`가 필요할 경우 쉽게 추가 가능.



