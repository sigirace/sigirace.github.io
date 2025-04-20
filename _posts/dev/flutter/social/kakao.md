### 1. 라이브러리 설치

- kakao developer > 문서 > flutter > 시작하기
- 설치

```
dependencies:
  kakao_flutter_sdk: ^1.9.5 # 전체 추가
  kakao_flutter_sdk_user: ^1.9.5 # 카카오 로그인 API 패키지
  kakao_flutter_sdk_share: ^1.9.5 # 카카오톡 공유 API 패키지
  kakao_flutter_sdk_talk: ^1.9.5 # 카카오톡 채널, 카카오톡 소셜, 카카오톡 메시지 API 패키지
  kakao_flutter_sdk_friend: ^1.9.5 # 피커 API 패키지
  kakao_flutter_sdk_navi: ^1.9.5 # 카카오내비 API 패키지
```



### 2. 초기화

```dart
// 웹 환경에서 카카오 로그인을 정상적으로 완료하려면 runApp() 호출 전 아래 메서드 호출 필요
WidgetsFlutterBinding.ensureInitialized();

// runApp() 호출 전 Flutter SDK 초기화
KakaoSdk.init(
    nativeAppKey: '${YOUR_NATIVE_APP_KEY}',
    javaScriptAppKey: '${YOUR_JAVASCRIPT_APP_KEY}',
);
```



### 3. 플랫폼

- 내어플리케이션 > 앱설정 > 앱키
- 내어플리케이션 > 앱설정  > 플랫폼

**3.1 Android**

- pacakge 설정
  - android > app > src > main > AndroidManifest.xml
  - social > AndroidManifest.md 파일 확인

- 키 해시 생성
  - 디버그/ 릴리즈 환경에 맞춰 사용 (플랫폼 > 가이드 확인하기)
  - 릴리즈에는 한번 더 생성해줘야 함


```
keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore -storepass android -keypass android | openssl sha1 -binary | openssl base64
```

- 인터넷 설정
  - android > app > src > main > AndroidManifest.xml

```
<uses-permission android:name="android.permission.INTERNET" />
```



**3.2 ios**

- ios 폴더 우클릭 > Open in Xcode
  - Runner > General > Identity > Bundle Identifier 복사



### 4. 프로젝트 설정

- 스킴: 카카오로 갔다가 다시 앱으로 돌아옴

**4.1 Android**

- android > app > src > main > AndroidManifest.xml
- application 안의 activity 위에 복붙

```
<application

		<!-- 카카오 로그인 커스텀 URL 스킴 설정 -->
    <activity 
        android:name="com.kakao.sdk.flutter.AuthCodeCustomTabsActivity"
        android:exported="true">
        <intent-filter android:label="flutter_web_auth">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />

            <!-- "kakao${YOUR_NATIVE_APP_KEY}://oauth" 형식의 앱 실행 스킴 설정 -->
            <!-- 카카오 로그인 Redirect URI -->
            <data android:scheme="kakao${YOUR_NATIVE_APP_KEY}" android:host="oauth"/>
        </intent-filter>
    </activity>
    
    <activity ...>
```



**4.2 ios**

- 문서에 ios 하위 앱 실행 허용 목록
- Ios > Runner > Info.plist

```
<dict>
...
	<key>LSApplicationQueriesSchemes</key>
    <array>
      <!-- 카카오톡으로 로그인 -->
      <string>kakaokompassauth</string>
      <!-- 카카오톡 공유 -->
      <string>kakaolink</string>
      <!-- 카카오톡 채널 -->
      <string>kakaoplus</string>
    </array>
</dict>
```

- ios 폴더 우클릭 > Open in Xcode
  - Runner > Info > URL Types
  - URL Schemes : kakao[native_app_key]



### 5. 카카오 로그인

- 내 어플리케이션 > 제품설정 > 카카오 로그인 > 활성화 설정
- OpenId는 파이어베이스
- 문서 > 카카오 로그인 > flutter
  - 디자인 가이드
  - 카카오 로그인 구현 예제



















