---
layout: single
title:  '[생성#2] Factory Method'
toc: true
categories: Python
tags: [Factory pattern, Python, 생성패턴]

---

📜 [참조문서](https://refactoring.guru/ko/design-patterns/facade)
{: .notice}

## 👀 목적

> 변경에는 닫혀있고, 확장에는 열려있는 생성 구조를 만드는 것 (`OCP`)

- 어떤 인스턴스를 만들지 서브 클래스가 정하는 패턴
- 기능 혹은 역할에 따른 구현체가 존재하고, 그 중에서 특정한 구현체를 만들 수 있는 다양한 팩토리(`Creator`)를 제공할 수 있음

## ⚙️ 구성요소

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/design_patterns/factory_method.png?raw=true" width="600" height="250"></p>

- `Product`: 
- `Concrete Product`: 
- `Creator`: 
- `Concrete Creator`: 



📌 **비즈니스 로직을 구상 제품과 분리하는 이유**

**1. 결합도 감소**: 비즈니스 로직이 구체적인 제품 클래스에 포함되어 있으면, **제품 클래스와 비즈니스 로직이 강하게 결합**됩니다. 이렇게 되면 비즈니스 로직을 수정할 때마다 제품 클래스를 수정해야 하므로, **변경에 따른 영향 범위가 넓어지고 유지보수**가 어려워집니다. 반면, **비즈니스 로직을 별도의 팩토리나 서비스 계층**으로 분리하면 구체적인 제품 클래스는 단순히 데이터만 보유하거나 특정 기능만 수행하고, 비즈니스 로직 변경이 다른 코드에 미치는 영향을 최소화할 수 있습니다.

**2. Single Responsibility Principle (단일 책임 원칙)**: 제품 클래스는 특정 데이터를 보유하거나 기능을 수행하는 역할에 집중하고, 비즈니스 로직은 비즈니스 규칙을 관리하는 역할에 집중하는 것이 좋습니다. 이를 통해 **단일 책임 원칙(SRP)**을 지키고, 각 클래스가 하나의 책임에 집중하도록 할 수 있습니다. 비즈니스 로직이 제품 클래스에 포함되면 제품 클래스가 여러 역할을 수행하게 되므로, **역할의 명확성**이 떨어지고 유지보수가 어려워질 수 있습니다.



## 💡 구현 방법

1. 모든 제품이 같은 인터페이스를 따르도록 설정
   - 이 인터페이스는 모든 제품에서 의미가 있는 메서드들을 선언해야 합니다.
2. 크리에이터 클래스 내부에 빈 팩토리 메서드를 추가
   - 이 메서드의 반환 유형은 공통 제품 인터페이스와 일치해야 합니다.
3. 제품 생성자들에 대한 코드들을 팩토리 메소드에 대한 호출로 교체
   - 제품의 유형을 구분하기 위해 팩토리 메서드에 임시 매개변수를 추가해야 할 수도 있음
   - 이 시점에서 팩토리 메서드의 코드는 꽤 복잡할 수 있다. 예를 들어 인스턴트화할 제품 클래스를 선택하는 큰 `switch` 문장



## 🌈 구현 예제

**프로젝트 구조**

```

```







```
class Ship {
    String name, color, capacity;

    @Override
    public String toString() {
        return String.format("Ship { name: '%s', color: '%s', logo: '%s' }", name, color, capacity);
    }
}

public static Ship orderShip(String name, String email) {
    if (name == null) {
        throw new IllegalArgumentException("배 이름을 지어주세요");
    }
    if (email == null) {
        throw new IllegalArgumentException("이메일을 남겨주세요");
    }

    // 선박 객체 생성
    Ship ship = new Ship();

    // 선박 객체 생성 후처리
    ship.name = name;

    if (name.equalsIgnoreCase("ContainerShip")) {
        ship.capacity = "20t";
    } else if (name.equalsIgnoreCase("OilTankerShip")) {
        ship.capacity = "15t";
    }

    if (name.equalsIgnoreCase("ContainerShip")) {
        ship.color = "green";
    } else if (name.equalsIgnoreCase("OilTankerShip")) {
        ship.color = "blue";
    }

    System.out.println(ship.name + " 다 만들었다고 " + email + "로 메일을 보냈습니다.");

    return ship;
}

public static void main(String[] args) {
    Ship containerShip = orderShip("ContainerShip", "inpa.naver.com");
    System.out.println(containerShip);

    Ship oilTankerShip = orderShip("OilTankerShip", "inpa.naver.com");
    System.out.println(oilTankerShip);
}

이걸 결제와 관련하여 내용(카카오페이 결제, 삼성카드결제, 무통장 거래)을 바꿔주고 python 코드로 생성해줘
```





```
이제 저 코드를 아래와 같이 팩토리 메서드 패턴으로 변경해줘

class Ship {
    String name, color, capacity;

    @Override
    public String toString() {
        return String.format("Ship { name: '%s', color: '%s', logo: '%s' }\n", name, color, capacity);
    }
}

class ContainerShip extends Ship {
    ContainerShip(String name, String capacity, String color) {
        this.name = name;
        this.capacity = capacity;
        this.color = color;
    }
}

class OilTankerShip extends Ship {
    OilTankerShip(String name, String capacity, String color) {
        this.name = name;
        this.capacity = capacity;
        this.color = color;
    }
}

abstract class ShipFactory {

    // 객체 생성 전처리 / 후처리 메서드 (상속 불가)
    final Ship orderShip(String email) {
        validate(email);

        Ship ship = createShip(); // 선박 객체 생성

        sendEmailTo(email, ship);

        return ship;
    }

    // 팩토리 메서드
    abstract protected Ship createShip();

    private void validate(String email) {
        if (email == null) {
            throw new IllegalArgumentException("이메일을 남겨주세요");
        }
    }

    private void sendEmailTo(String email, Ship ship) {
        System.out.println(ship.name + " 다 만들었다고 " + email + "로 메일을 보냈습니다.");
    }
}

class ContainerShipFactory extends ShipFactory {
    @Override
    protected Ship createShip() {
        return new ContainerShip("ContainerShip", "20t", "green");
    }
}

class OilTankerShipFactory extends ShipFactory {
    @Override
    protected Ship createShip() {
        return new OilTankerShip("OilTankerShip", "15t", "blue");
    }
}

class Client {
    public static void main(String[] args) {
        // 전용 선박 생산 공장 객체를 통해 선박을 생성
        Ship containerShip = new ContainerShipFactory().orderShip("inpa.naver.com");
        System.out.println(containerShip);

        Ship oilTankerShip = new OilTankerShipFactory().orderShip("inpa.naver.com");
        System.out.println(oilTankerShip);
    }
}
```





```
개방폐쇄원칙에 맞게 다시 작성하고
전략의 구성요소: context, strategy, concretestrategies
팩토리메서드의 구성요소: creator, concreteCreator, product, concreteProduct를 모두 표기



django restframework 및 APIView를 사용하며 서비스레이어를 따로 구성

서비스레이어는 service 폴더 하위에 두도록
```



