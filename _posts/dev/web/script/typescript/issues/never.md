## 📍never 형식 오류

'never' 형식 오류는 TypeScript에서 발생하는 오류로, 특정 값이 절대 발생하지 않거나, 특정 타입이 존재하지 않을 때 나타납니다. 주로 다음과 같은 경우에 발생합니다:

1. 타입 추론 실패: TypeScript가 변수의 타입을 추론할 수 없을 때, 기본적으로 'never' 타입으로 간주할 수 있습니다. 예를 들어, useRef를 사용할 때 타입을 명시하지 않으면, TypeScript는 ref.current의 타입을 알 수 없어서 'never'로 간주할 수 있습니다.
2. 잘못된 타입 사용: 함수가 항상 예외를 던지거나 무한 루프에 빠지는 경우, TypeScript는 해당 함수가 절대 정상적으로 종료되지 않음을 인식하고 'never' 타입을 반환합니다.

조건부 타입: 조건부 타입에서 모든 경우의 수를 처리하지 않으면, TypeScript는 'never' 타입을 반환할 수 있습니다.

이 오류를 해결하려면, 변수나 함수의 타입을 명시적으로 지정하거나, 모든 경우의 수를 처리하도록 코드를 수정해야 합니다. 예를 들어, useRef의 경우, useRef<HTMLDivElement | null>(null)와 같이 타입을 명시해 주면 오류를 해결할 수 있습니다.



🌈 **예시**

```typescript
const useFadeIn = ({duration, delay}: FadeInProps) => {
    const ref = useRef(null);

    useEffect(() => {
        setTimeout(() => {
          if (ref.current) {
            ref.current.style.opacity = "1";
            ref.current.style.transition = `opacity ${duration}s ease-in-out`;
          }
        }, delay);
      }, []);

}
```

- useRef에 제네릭이 없음

```typescript
const useFadeIn = ({duration, delay}: FadeInProps) => {
    const ref = useRef<HTMLDivElement | null>(null); // ref의 타입을 명시적으로 설정

    useEffect(() => {
        setTimeout(() => {
          if (ref.current) {
            ref.current.style.opacity = "1";
            ref.current.style.transition = `opacity ${duration}s ease-in-out`;
          }
        }, delay);
      }, []);
}
```

