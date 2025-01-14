### 📍 TextFiled

- **width**: 부모 제약
- **height**: maxLines, minLines에 의해 결정
  - 둘은 함께 사용되어야 함
  - maxLines가 null이면 제약이 없다는 뜻
- **controller**: TextEdittingController
- **onEditting**: 키보드의 done 누를시 수행할 function
- **autocorrect**: 키보드 자판에서 자동 수정 추천 볼것인지 결정
- **keyboardtype**: 키보드 자판의 유형
- **obscureText**: 비밀번호 표시 (true/false)
- **decorator**
  - **focused**: 쓰려고 클릭할 때, UnderlineInput, Border로 색상지정
  - **enabled**: 대기 상태일때, UnderlineInput, Border로 색상지정
  - **hint/error**: 힌트와 에러

### 📍TextFormForm

- **validator**: 콜백, 입력된 값에 대한 검증 수행 -> 검증 통과 못하면 아래 에러메세지 도출
- **onSave**: 콜백 -> 폼에 있는 값들을 수행
