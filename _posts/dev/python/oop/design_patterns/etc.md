**1. 생성(Creational) 패턴**

> 객체를 어떻게 **효율적으로 생성**할 것인가에 초점.

- 객체 생성 로직을 캡슐화.
- 객체 생성 시 특정 조건이나 상황에 따라 생성 방식을 변경 가능.



**2. 구조(Structural) 패턴**

> 객체 간 **구조적인 관계**를 정의하여 **조직화와 확장성**을 제공.

- 객체 간의 인터페이스를 단순화하거나, 다수의 객체를 효율적으로 구성.
- 기존의 클래스나 객체를 재사용하기 위한 구조 제공.
- 시스템의 유연성과 확장성을 강화.



**3. 행동(Behavioral) 패턴**

> **객체 간의 상호작용**과 **책임 분배**를 관리하는 데 초점을 맞춥니다.

- 객체나 클래스가 협력하는 방식과 상호작용을 정의.
- 실행 중인 프로그램에서 객체 간의 동적인 상호작용을 조정.
- 책임을 명확히 하여 유지보수를 용이하게 함.

​	



- **전략 패턴 (Strategy)**  
  - **적용 상황**: **`상황에 따라 다른 기능`**을 사용해야 할 때 적용
  - **특징**:  
    - 전략을 선택하는 것(컨텍스트)과 실행하는 것(전략, 알고리즘)의 책임을 분리
    - 새로운 로직(전략)을 추가해도 기존 코드를 수정하지 않음(OCP 준수)
    - 팩토리 메서드와 연계하여 적용
  
- **팩토리 메서드 패턴 (Factory Method)**  
  - **적용 상황**: **`상황에 따라 다른 객체`**를 생성해야 할 때 과도한 if-else가 발생할 때 적용
  - **특징**:  
    - 객체 생성 로직을 팩토리 메서드로 캡슐화하여 유지보수성과 확장성을 확보.  
    - if-else로 구성된 로직을 제거하여 OCP를 준수.  
  
- **데코레이터 패턴 (Decorator)**  
  
  - **적용 상황**: 객체의 조합을 통해 **`기능을 확장`**하여 사용하려고 할 때 적용
  - **특징**:  
    - 상속을 통해 새로운 객체를 만들어낸다면, 클래스 폭발 문제가 발생.  
    - 데코레이터를 사용하여 기능을 동적으로 추가하고, 기능의 조합과 순서를 자유롭게 변경 가능.  
  
- **옵저버 패턴 (Observer)**
  - **적용 상황**: 일대다 의존성을 가진 시스템에서 효율적인 이벤트 핸들링을 구현하고 싶을 때 적용
  - **특징**
    - 옵저버가 많아질수록 알림 전파 비용이 증가하기에 큐 기반 비동기 처리(celery)를 고려
  
- **어댑터 패턴 (Adapter)**
  
  - **적용 상황**
    - 이미 존재하는 기능을 가진 클라이언트에 같은 기능을 하는 새로운 API 혹은 서비스를 추가하려 할 때, 인터페이스가 호환되지 않을 경우 사용
    - 부모 클래스를 수정할 수 없는 상황(이미 완성 혹은 framework api 등)에서 자식 클래스를 확장하고 싶을 때 사용
  
  - **특징**
    - 모든 자식 클래스를 수정하여 확장하는 것은 코드 중복이 발생함
  
  





📌 **일대다 의존성**

> 하나의 주체(이벤트 발생자)가 여러 구독자(옵저버, 이벤트에 관심있는 객체)에게 이벤트를 전달함



📌 **캡슐화**

- 객체의 속성(변수)과 행위(함수)를 묶음으로써 데이터와 로직이 하나의 단위로 독립적으로 동작하며, 필요한 부분만 인터페이스를 통해 노출함으로써 재사용성을 높입니다. 👉 **재사용성 증가**
- 외부에서 객체의 세부 구현에 접근하지 못하도록 보호하는 동시에, 인터페이스를 통해 객체 간 결합도를 낮추어 코드 변경 시 영향을 최소화합니다. 👉 정보 은닉
- Getter와 Setter는 데이터 접근을 완전히 노출하는 대신, 필요한 경우에만 제공하여 객체의 데이터 무결성을 보장합니다. 불필요한 Getter와 Setter는 캡슐화의 취지를 약화시킬 수 있습니다. 👉 데이터 무결성
- 캡슐화를 통해 객체는 외부 세계에 노출된 인터페이스만 의존하므로, 내부 구현 변경 시에도 외부 코드는 영향을 받지 않습니다. 👉 객체간 의존성 줄임



📌 **결합도**

> 한 객체가 다른 객체에 얼마나 강하게 의존하는지를 나타내는 척도

- 결합도가 높음 👉 한 객체의 변경이 다른 객체에 영향을 미칠 가능성이 커짐
- 결합도가 낮음 👉 유지보수성과 확장성이 높음



📌 **인터페이스와 결합도**

- 인터페이스를 사용하면 객체는 구체적인 클래스가 아니라 추상적인 인터페이스에 의존  👉 간접의존
- 객체가 추상적으로 무엇을 해야하는지 알지만 구체적인 내용은 모름
- 의존성 주입시 인터페이스에 맞게 구현하기만 하면 결합할 수 있으므로 다양하게 사용 가능



🌈 **예제: 직접 의존, 결합도 높은 코드**

```python
class PayPal:

  def pay(self, amount):
    print(f"PayPal로 {amount} 결제 완료")

class PaymentProcessor:

  def __init__(self):
    self.payment_method = PayPal() # PayPal 클래스에 직접 의존

  def process_payment(self, amount):
    self.payment_method.pay(amount)


# 사용
processor = PaymentProcessor()
processor.process_payment(100)
```

⛔️ **문제점**

- 생성자에서 다른 클래스를 직접 의존하고 있음
- 새로운 payment_method에 대해 PaymentProcessor 클래스 사용 불가 👉 확장성과 유지보수성 떨어짐



🌈 **예제: 인터페이스, 결합도 낮춘 코드**

📒 **interface.py**

```Python
from abc import ABC, abstractmethod

class Payment(ABC):

  @abstractmethod
  def pay(self, amount): # 이 클래스는 결제 기능이 있어야함 => 추상적인 기능 정의
    pass
```

📒 **payment_methods.py**

```python
# 결제 방식들은 결제 클래스를 구현함 -> 추상적인 기능을 자신의 입맛에 맞게 실체화
class PayPal(Payment):
  
  def pay(self, amount):
    print(f"PayPal로 {amount} 결제 완료") # PayPal 결제 로직

class Stripe(Payment):
  
  def pay(self, amount):
    print(f"Stripe로 {amount} 결제 완료") # Stripe 결제 로직
```

📒 **payment_processor.py**

```python
class PaymentProcessor:
  def __init__(self, payment: Payment): # 인터페이스로 의존성 주입
    self.payment_menthod = payment

  def process_payment(self, amount):
    self.payment_menthod.pay(amount)
```

📒 **main.py**

```python
paypal_gateway = PayPal()
processor = PaymentProcessor(paypal_gateway)
processor.process_payment(100)

stripe_gateway = Stripe()
processor = PaymentProcessor(stripe_gateway)
processor.process_payment(200)
```

- 새로운 결제 방식이 추가되어도 인터페이스 따르는 객체를 주입하여 의존성 해결







📌 **표준화된 인터페이스**

- 모든 객체가 





좋은 질문입니다! **“ㄹ”**는 뜻을 쉽게 설명하겠습니다.



**1. 표준화된 인터페이스란?**



표준화된 인터페이스는 **모든 결제 게이트웨이가 동일한 방식으로 동작하도록 만든 규칙**입니다.

​	•	예를 들어, 모든 게이트웨이는 pay(amount)와 refund(transaction_id)라는 메서드를 제공해야 한다는 규칙을 정한 것입니다.

​	•	이 규칙을 기반으로 뷰(APIView)는 어떤 게이트웨이를 사용하더라도 동일한 방식으로 호출할 수 있습니다.



**표준화된 인터페이스의 역할**

​	•	뷰는 “결제 처리”라는 동작에만 집중하고, PayPal, Stripe, KakaoPay 등의 내부 구현 방식은 몰라도 됩니다.

​	•	이를 통해 뷰는 다양한 게이트웨이와 “독립적”으로 동작할 수 있습니다.



**2. 게이트웨이의 구현 세부 사항이란?**



각 게이트웨이는 고유한 API를 가지고 있어 호출 방식이 다릅니다.



**PayPal의 구현 세부 사항**

​	•	결제 요청: send_payment(amount)

​	•	환불 요청: process_refund(transaction_id)



**Stripe의 구현 세부 사항**

​	•	결제 요청: charge(amount)

​	•	환불 요청: reverse_charge(transaction_id)



**KakaoPay의 구현 세부 사항**

​	•	결제 요청: pay(amount)

​	•	환불 요청: refund(transaction_id)



이처럼 각 게이트웨이의 API 메서드 이름, 매개변수 등이 다릅니다.



**3. 표준화된 인터페이스만 사용하면 어떤 일이 일어나는가?**



뷰는 게이트웨이의 구현 세부 사항을 전혀 알 필요가 없습니다. Adapter가 각 게이트웨이의 세부 사항을 처리해주기 때문입니다.



**뷰(APIView)의 코드 예제**



*# 표준화된 인터페이스만 호출*

transaction_id = payment_service.process_payment(amount)



뷰는 process_payment를 호출할 뿐입니다. **어떤 게이트웨이를 사용하는지, 내부적으로 어떤 API를 호출하는지는 Adapter가 알아서 처리**합니다.



**4. 예를 들어 설명**



**표준화된 인터페이스가 없는 경우**

​	•	뷰에서 각 게이트웨이의 구현 세부 사항을 알아야 하고, 게이트웨이가 추가될 때마다 뷰 코드를 수정해야 합니다.



*# 뷰에서 직접 각 게이트웨이를 처리*

if gateway == "paypal":

  paypal = PayPalAPI()

  transaction_id = paypal.send_payment(amount)

elif gateway == "stripe":

  stripe = StripeAPI()

  transaction_id = stripe.charge(amount)

elif gateway == "kakaopay":

  kakaopay = KakaoPayAPI()

  transaction_id = kakaopay.pay(amount)



**표준화된 인터페이스를 사용하는 경우**

​	•	뷰는 게이트웨이의 내부 동작을 몰라도 됩니다. 게이트웨이를 관리하는 Adapter와 Service가 내부 구현을 처리합니다.



*# 뷰는 표준화된 인터페이스만 호출*

transaction_id = payment_service.process_payment(amount)



​	•	PayPalAdapter, StripeAdapter, KakaoPayAdapter가 각각의 게이트웨이 호출 방식을 처리하기 때문에, 뷰는 단일 인터페이스(process_payment)만 호출하면 됩니다.



**5. 주요 장점**

​	1.	**유지보수 용이성**:

​	•	새로운 게이트웨이가 추가되거나 기존 게이트웨이가 변경되어도 Adapter와 Service만 수정하면 됩니다. 뷰(APIView)는 수정하지 않아도 됩니다.

​	2.	**코드 간 결합도 감소**:

​	•	뷰는 게이트웨이의 동작 방식을 전혀 몰라도 되므로, 뷰 코드와 게이트웨이 로직이 독립적으로 유지됩니다.

​	3.	**확장성 증가**:

​	•	표준화된 인터페이스를 유지하면 새로운 게이트웨이를 쉽게 추가할 수 있습니다. 새로운 Adapter만 작성하면 뷰는 기존 코드로 계속 작동합니다.



**비유로 설명**

​	•	표준화된 인터페이스는 **전원 멀티탭**과 같습니다.

​	•	각 결제 게이트웨이는 다른 모양(플러그)을 가지고 있습니다(PayPal, Stripe, KakaoPay).

​	•	Adapter는 다양한 플러그를 하나의 표준 인터페이스(멀티탭)에 맞게 변환해줍니다.

​	•	뷰(APIView)는 멀티탭만 사용하므로, 어떤 플러그든 잘 작동합니다.



**결론**

​	•	“뷰(APIView)는 표준화된 인터페이스만 사용하므로 게이트웨이의 구현 세부 사항에 의존하지 않는다”는 말은:

​	•	뷰는 “결제를 처리하라”는 명령만 내리고, 구체적으로 어떤 API 메서드가 호출되는지 알 필요가 없다는 뜻입니다.

​	•	Adapter가 모든 세부 사항을 처리하여 뷰와 게이트웨이 사이의 중간 다리 역할을 합니다.

​	•	이를 통해 유지보수성과 확장성을 크게 향상시킬 수 있습니다.
