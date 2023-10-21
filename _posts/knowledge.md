github 자격증명(window) : https://velog.io/@rimo09/Github-%EC%9C%88%EB%8F%84%EC%9A%B0-git-credential-access-token-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0

wandb

entity: 상위 폴더 이름 (팀/ 개인)

project: 프로젝트 이름

name: 실험 이름



코랩 세션 끊김



```
function ClickConnect(){
    console.log("코랩 연결 끊김 방지"); 
    document.querySelector("colab-toolbar-button#connect").click() 
}
setInterval(ClickConnect, 60 * 1000)
```