[poetry]

👀 **Definitions**

> python package를 설치하고 관리할 수 있게 함

**1. 환경 생성**

```
poetry init

# 환경 구성
pacakge name
enter (skip)
- no
- no
- yes
```

**2. 환경 확인**

- pyproject.toml

**3. 의존성 추가**

```
poetry add [package]
```

**4. 환경 접근**

```
poetry shell
```

**5. 환경 종료**

```
exit
```



### Ubuntu 설치

```
apt update
apt install curl -y
apt install python3 python3-pip -y
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```



### python 3.11

```
apt install vim -y
apt install python3.11 python3.11-venv python3.11-dev -y
poetry env use python3.11
poetry shell
```

