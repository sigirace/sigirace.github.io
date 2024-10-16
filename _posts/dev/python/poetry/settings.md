### 1. 파이썬 설치

```
apt update
apt install sudo curl vim -y
sudo apt update

sudo apt install python3.11 python3.11-venv python3.11-dev -y
```

### 2. Poetry 설치

```
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc  # 또는 ~/.zshrc
```

### 3. poetry 설정

```
poetry init
poetry shell
```

### ❤️‍🔥 Issue

```
root@7fc5425dd2ee:~/app# poetry shell
The currently activated Python version 3.10.12 is not supported by the project (^3.11).
Trying to find and use a compatible version.
Using python3.11 (3.11.0)
Virtual environment already activated: /root/.cache/pypoetry/virtualenvs/flask-api-cEwzT8cw-py3.11
root@7fc5425dd2ee:~/app#
```

위와 같이 나올 경우

```
exit
```

