## **🚀 팩토리 메서드 패턴(Factory Method Pattern)란?**

### **📌 개념**

팩토리 메서드 패턴(Factory Method Pattern)은 **객체의 생성(인스턴스화) 과정을 서브클래스에서 결정하도록 하는 디자인 패턴**입니다.
즉, **객체를 직접 생성하지 않고, 하위 클래스에서 인스턴스를 만들도록 위임하는 방식**입니다.

📌 **핵심 포인트**

> **클래스 내부에서 객체를 생성하는 전용 메서드(팩토리 메서드)를 제공**하여 객체 생성을 캡슐화(=감춤).

- 이로인해 클라이언트 코드에서 객체를 직접 생성하지 않음.
- 따라서, 객체 생성 방식이 변경되어도 클라이언트 코드에 영향을 주지 않음.



## ⛔️ 문제점1: 클라이언트 코드 수정

📒 **Class 정의**

```python
class Product:
    def operation(self):
        return "Product created!"
```

🕹️ **Client 코드**

```python
product = Product()  # ❌ 직접 생성 (하드코딩됨)
print(product.operation())
```



### 💬 문제 도출

>🧐 **별문제 없어 보이는데..?**
>
>🧑‍💻 **만약 Product의 유형이 늘어난다면?**



📒 **Class 재정의**

```python
class ProductA:
    def operation(self):
        return "Product A created!"

class ProductB:
    def operation(self):
        return "Product B created!"
```



🤪 **Client 코드 수정**

```python
# ❌ 클라이언트 코드가 직접 객체를 생성해야 함
product_type = "A"

if product_type == "A":
    product = ProductA()
elif product_type == "B":
    product = ProductB()
else:
    raise ValueError("Unknown product type")

print(product.operation())  # Product A created!
```



## ✅ 패턴 적용

📒 **Class 정의**

```python
class ProductA:
    def operation(self):
        return "Product A created!"

class ProductB:
    def operation(self):
        return "Product B created!"

class ProductFactory:
    @classmethod
    def create_product(cls, product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
        else:
            raise ValueError("Unknown product type")
```

🕹️ **Client 코드**

```python
product = ProductFactory.create_product("A")
print(product.operation())  # Product A created!

product = ProductFactory.create_product("B")
print(product.operation())  # Product B created!
```



### 💡 개선된 점

> 😀 : **Product의 유형이 아무리 늘어나도 클라이언트의 코드에는 영향을 주지 않음, 단지 `create_product`의 인자만 바꿔주면 됨**





⛔️ 문제점1: 클라이언트 코드 수정



```python
class Product:
    def operation(self):
        return "Base Product"

class CustomProduct(Product):
    def operation(self):
        return "Custom Product"
```





```python
product = CustomProduct()  # 직접 생성
print(product.operation())  # Custom Product
```







```python
# [원본 코드] - PaymentService가 구체 클래스를 직접 생성하는 방식

class PaymentGateway(ABC):
  
  	@abstractmethod
    def process_payment(self, amount):
        """외부 결제 API와 연동하여 결제를 처리합니다."""
        raise NotImplementedError("반드시 하위 클래스에서 구현해야 합니다.")

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        # 복잡한 PayPal API 연동 로직 (인증, 거래 실행, 응답 파싱 등)
        # 예를 들어, 실제 API 호출 후 응답에서 transaction_id를 획득한다고 가정
        transaction_id = "paypal_txn_123456"
        # 추가 비즈니스 로직: 결제 기록 업데이트, 사용자 알림 등
        return transaction_id

class StripePayment(PaymentGateway):
    def process_payment(self, amount):
        # 복잡한 Stripe API 연동 로직
        transaction_id = "stripe_txn_654321"
        # 추가 비즈니스 로직: 주문 상태 갱신, 로깅 등
        return transaction_id

class PaymentService:
    def __init__(self, payment_method):
        # 클라이언트가 전달한 payment_method에 따라 구체 클래스를 직접 생성함
        if payment_method == "paypal":
            self.gateway = PayPalPayment()
        elif payment_method == "stripe":
            self.gateway = StripePayment()
        else:
            raise ValueError("지원하지 않는 결제 방식입니다.")

    def execute_payment(self, amount):
        # 추가 비즈니스 로직: 금액 검증, 트랜잭션 로깅 등
        transaction_id = self.gateway.process_payment(amount)
        # 주문 업데이트, 사용자 통지 등 추가 처리
        return transaction_id

# 클라이언트 사용 예시
service = PaymentService("paypal")
txn_id = service.execute_payment(150.00)
print("Transaction ID:", txn_id)
```



```python
# 새로운 결제 수단: SquarePayment 클래스 추가
class SquarePayment(PaymentGateway):
    def process_payment(self, amount):
        # Square API와의 복잡한 연동 로직 (인증, 거래 실행, 응답 처리 등)
        transaction_id = "square_txn_789012"
        # 추가 비즈니스 로직: Square 전용 로깅, 상태 업데이트 등
        return transaction_id

# PaymentService 수정: 새로운 분기를 추가
class PaymentService:
    def __init__(self, payment_method):
        if payment_method == "paypal":
            self.gateway = PayPalPayment()
        elif payment_method == "stripe":
            self.gateway = StripePayment()
        elif payment_method == "square":
            self.gateway = SquarePayment()  # 새롭게 추가된 부분
        else:
            raise ValueError("지원하지 않는 결제 방식입니다.")

    def execute_payment(self, amount):
        transaction_id = self.gateway.process_payment(amount)
        return transaction_id

# 클라이언트 사용 예시: Square 결제 방식 사용
service = PaymentService("square")
txn_id_modified = service.execute_payment(250.00)
print("Transaction ID:", txn_id_modified)
```









```python
# [팩토리 메서드 적용 코드]

# 기존 결제 게이트웨이 클래스(PayPalPayment, StripePayment)는 그대로 사용
class PaymentGatewayFactory:
    def create_gateway(self, payment_method):
        if payment_method == "paypal":
            return PayPalPayment()
        elif payment_method == "stripe":
            return StripePayment()
        else:
            raise ValueError("지원하지 않는 결제 방식입니다.")

class PaymentServiceWithFactory:
    def __init__(self, payment_method, factory=None):
        # 팩토리 주입: 기본적으로 PaymentGatewayFactory를 사용하되,
        # 외부에서 다른 팩토리(예: 커스터마이즈된 팩토리)를 주입할 수 있음
        self.factory = factory if factory is not None else PaymentGatewayFactory()
        self.gateway = self.factory.create_gateway(payment_method)

    def execute_payment(self, amount):
        transaction_id = self.gateway.process_payment(amount)
        return transaction_id

# 클라이언트 사용 예시
service_factory = PaymentServiceWithFactory("stripe")
txn_id_factory = service_factory.execute_payment(200.00)
print("Transaction ID:", txn_id_factory)
```



```python
# SquarePayment 클래스는 위와 동일하게 사용

# PaymentGatewayFactory 수정: square 분기를 추가
class PaymentGatewayFactory:
    def create_gateway(self, payment_method):
        if payment_method == "paypal":
            return PayPalPayment()
        elif payment_method == "stripe":
            return StripePayment()
        elif payment_method == "square":
            return SquarePayment()  # 새롭게 추가된 부분
        else:
            raise ValueError("지원하지 않는 결제 방식입니다.")

# PaymentService는 변경 없이 동일한 인터페이스를 사용
class PaymentService:
    def __init__(self, payment_method, factory=None):
        self.factory = factory if factory is not None else PaymentGatewayFactory()
        self.gateway = self.factory.create_gateway(payment_method)

    def execute_payment(self, amount):
        transaction_id = self.gateway.process_payment(amount)
        return transaction_id

# 클라이언트 사용 예시: Square 결제 방식 사용
service = PaymentService("square")
txn_id_factory = service.execute_payment(300.00)
print("Transaction ID:", txn_id_factory)
```

