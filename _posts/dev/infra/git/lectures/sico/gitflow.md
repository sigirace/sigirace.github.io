### version

0.0.0

- first: major
- second: feature
- third: bug

[img / git_tutorial.gitflow]



### example

**1. git remote 연결**

**2. git flow setting**

```
git flow init
```

- release branch 확인
  - Branch name for production releases: [main]
  - github의 default를 확인하고 맞춰주어야함

**3. develop push**

```
git push origin --all
```

**4. feature branch 생성**

```
git flow feature start login
git flow feature start regist
```

- login/ regist는 feature name

**5. feature branch push**

```
git push -u origin feature/login
git push -u origin feature/regist
```

**6. feature coding**

**feature/login**

```python
class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def login(self):
        print(f"Login with {self.id} and {self.password}")
```

```
git add .
git commit -m "feat: login 기능 구현"
git push
```

**feature/regist**

```python
class Common:

    def __init__(self):
        pass

    def hello(self):
        print("Hello, World!")
```

```
git add .
git commit -m "feat: common 기능구현" 
```



**7. pull & request**

- [github] feature/login 브랜치에서 pr 요청

```
@[id] 
리뷰 요청
```

- [github] 승인 후 close with comment > 승인은 가장 마지막 커밋에 있는 코드를 보고 결정
- [github] delete branch -> 삭제 못했다면 contribute > compare 

```
git flow feature finish login
```

```
Summary of actions:
- The feature branch 'feature/login' was merged into 'develop'
- Feature branch 'feature/login' has been removed
- You are now on branch 'develop'
```

- develop merge 및 feature branch 삭제
- 현재 branch는 develop

```
git push -u origin develop
```

- develop에 반영
- 다른 개발자들이 볼 수 있도록 하는게 좋음



**feature/regist**

```
git merge --no-ff develop
```

- 이미 끝나고 삭제된 login branch에서 merge할 수 없음



**8. release**

```
git flow release start 0.1.0
```

- 이슈 정리

```
git add .
git commit -m "release 0.1.0 completed"
git push -u origin release/0.1.0
```

- pr 진행 [위와 동일]

```
git flow release finish 0.1.0
```

- main, develop 등등 모두 반영됨

```
git push origin --all --follow-tags
```











