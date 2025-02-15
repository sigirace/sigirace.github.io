📍 **config 설정 확인**

```
git config --global -e
```

📍 **에디터 설정**

```
[core]
 editor = cursor --wait
```



📍 **글로벌 설정**

```
# 사용자 이름 설정
git config --global user.name "Your Name"

# 사용자 이메일 설정
git config --global user.email "your.email@example.com"
```

📍 **글로벌 설정 확인**

```
git config --global --list
```



📍 **로컬 설정**

```
# 사용자 이름 설정
git config user.name "Your Name"

# 사용자 이메일 설정
git config user.email "your.email@example.com"
```

- 로컬 설정은 글로벌 설정을 덮어씀
