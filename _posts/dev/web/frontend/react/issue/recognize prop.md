React does not recognize the `isActive` prop on a DOM element 경고 해결법
isActive를 $isActive나 isactive로 변경

이유 : React18 이후 일관성을 높이고, 사용자 혼동을 방지하기 위해 prop의 이름은 소문자나 앞에 $가 있어야만 사용자 지정 속성으로 인식함. $가 추가된 이유는 일부 라이브러리 또는 구성 요소는 대문자를 사용하는 prop을 요구하기 때문.



### 결론

> styled에 props 전달할때 $붙여서 변수명 설정하기

