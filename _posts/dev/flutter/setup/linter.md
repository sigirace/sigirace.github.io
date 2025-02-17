- 아래 옵션 설정 후 VSCode 에서 format on Save 켜고 저장

```plaintext
# analysis_options.yaml
linter:
  rules:
    require_trailing_commas: true
```

- 프로젝트 내 모든 파일에 적용

```plaintext
dart fix --apply
```

- CI check

```plaintext
dart fix --dry-run
```





```json
{
  "editor.formatOnSave": true,  // 저장할 때 자동 포맷
  "editor.formatOnType": true,  // 입력 중 자동 포맷
  "editor.defaultFormatter": "Dart-Code.dart-code",  // Dart 전용 포매터 설정
  "[dart]": {
    "editor.formatOnSave": true,
    "editor.formatOnType": true,
    "editor.defaultFormatter": "Dart-Code.dart-code"
  }
}
```

