## Constants Setup

`pubspec.yaml`

```dart
dependencies:
  flutter:
    sdk: flutter

  flex_color_scheme: ^7.3.1
  font_awesome_flutter: 10.3.0
  flutter_screenutil: ^5.9.3
```

`main.dart`

```dart
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:tiktok_clone_ver2/screens/sign_up_screen.dart';

void main() {
  runApp(const TikTokApp());
}

class TikTokApp extends StatelessWidget {
  const TikTokApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
        designSize: const Size(360, 690),
        builder: (_, child) {
          return MaterialApp(
            title: 'TikTok Clone',
            theme: ThemeData(
              primaryColor: const Color(0xFFE9435A),
              useMaterial3: true,
            ),
            home: const SignUpScreen(),
          );
        });
  }
}
```

- 메인 주석 정리
- build 아래 모두 지우기

### constants

- lib > constants

`sizes.dart`

```dart
class Sizes {
  static const size1 = 1.0;
  static const size2 = 2.0;
  static const size3 = 3.0;
  static const size4 = 4.0;
  static const size5 = 5.0;
  static const size6 = 6.0;
  static const size7 = 7.0;
  static const size8 = 8.0;
  static const size9 = 9.0;
  static const size10 = 10.0;
  static const size11 = 11.0;
  static const size12 = 12.0;
  static const size13 = 13.0;
  static const size14 = 14.0;
  static const size15 = 15.0;
  static const size16 = 16.0;
  static const size17 = 17.0;
  static const size18 = 18.0;
  static const size19 = 19.0;
  static const size20 = 20.0;
  static const size21 = 21.0;
  static const size22 = 22.0;
  static const size23 = 23.0;
  static const size24 = 24.0;
  static const size25 = 25.0;
  static const size26 = 26.0;
  static const size27 = 27.0;
  static const size28 = 28.0;
  static const size29 = 29.0;
  static const size30 = 30.0;
  static const size31 = 31.0;
  static const size32 = 32.0;
  static const size33 = 33.0;
  static const size34 = 34.0;
  static const size35 = 35.0;
  static const size36 = 36.0;
  static const size37 = 37.0;
  static const size38 = 38.0;
  static const size39 = 39.0;
  static const size40 = 40.0;
  static const size41 = 41.0;
  static const size42 = 42.0;
  static const size43 = 43.0;
  static const size44 = 44.0;
  static const size45 = 45.0;
  static const size46 = 46.0;
  static const size47 = 47.0;
  static const size48 = 48.0;
  static const size49 = 49.0;
  static const size50 = 50.0;
  static const size51 = 51.0;
  static const size52 = 52.0;
  static const size53 = 53.0;
  static const size54 = 54.0;
  static const size55 = 55.0;
  static const size56 = 56.0;
  static const size57 = 57.0;
  static const size58 = 58.0;
  static const size59 = 59.0;
  static const size60 = 60.0;
  static const size61 = 61.0;
  static const size62 = 62.0;
  static const size63 = 63.0;
  static const size64 = 64.0;
  static const size65 = 65.0;
  static const size66 = 66.0;
  static const size67 = 67.0;
  static const size68 = 68.0;
  static const size69 = 69.0;
  static const size70 = 70.0;
  static const size71 = 71.0;
  static const size72 = 72.0;
  static const size73 = 73.0;
  static const size74 = 74.0;
  static const size75 = 75.0;
  static const size76 = 76.0;
  static const size77 = 77.0;
  static const size78 = 78.0;
  static const size79 = 79.0;
  static const size80 = 80.0;
  static const size81 = 81.0;
  static const size82 = 82.0;
  static const size83 = 83.0;
  static const size84 = 84.0;
  static const size85 = 85.0;
  static const size86 = 86.0;
  static const size87 = 87.0;
  static const size88 = 88.0;
  static const size89 = 89.0;
  static const size90 = 90.0;
  static const size91 = 91.0;
  static const size92 = 92.0;
  static const size93 = 93.0;
  static const size94 = 94.0;
  static const size95 = 95.0;
  static const size96 = 96.0;
  static const size97 = 97.0;
  static const size98 = 98.0;
  static const size99 = 99.0;
  static const size100 = 100.0;
}
```

`gaps.dart`

```dart
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:tiktok_clone_ver2/constants/sizes.dart';

class Gaps {
  // Vertical Gaps
  static final v1 = SizedBox(height: Sizes.size1.w);
  static final v2 = SizedBox(height: Sizes.size2.w);
  static final v3 = SizedBox(height: Sizes.size3.w);
  static final v4 = SizedBox(height: Sizes.size4.w);
  static final v5 = SizedBox(height: Sizes.size5.w);
  static final v6 = SizedBox(height: Sizes.size6.w);
  static final v7 = SizedBox(height: Sizes.size7.w);
  static final v8 = SizedBox(height: Sizes.size8.w);
  static final v9 = SizedBox(height: Sizes.size9.w);
  static final v10 = SizedBox(height: Sizes.size10.w);
  static final v11 = SizedBox(height: Sizes.size11.w);
  static final v12 = SizedBox(height: Sizes.size12.w);
  static final v13 = SizedBox(height: Sizes.size13.w);
  static final v14 = SizedBox(height: Sizes.size14.w);
  static final v15 = SizedBox(height: Sizes.size15.w);
  static final v16 = SizedBox(height: Sizes.size16.w);
  static final v17 = SizedBox(height: Sizes.size17.w);
  static final v18 = SizedBox(height: Sizes.size18.w);
  static final v19 = SizedBox(height: Sizes.size19.w);
  static final v20 = SizedBox(height: Sizes.size20.w);
  static final v21 = SizedBox(height: Sizes.size21.w);
  static final v22 = SizedBox(height: Sizes.size22.w);
  static final v23 = SizedBox(height: Sizes.size23.w);
  static final v24 = SizedBox(height: Sizes.size24.w);
  static final v25 = SizedBox(height: Sizes.size25.w);
  static final v26 = SizedBox(height: Sizes.size26.w);
  static final v27 = SizedBox(height: Sizes.size27.w);
  static final v28 = SizedBox(height: Sizes.size28.w);
  static final v29 = SizedBox(height: Sizes.size29.w);
  static final v30 = SizedBox(height: Sizes.size30.w);
  static final v31 = SizedBox(height: Sizes.size31.w);
  static final v32 = SizedBox(height: Sizes.size32.w);
  static final v33 = SizedBox(height: Sizes.size33.w);
  static final v34 = SizedBox(height: Sizes.size34.w);
  static final v35 = SizedBox(height: Sizes.size35.w);
  static final v36 = SizedBox(height: Sizes.size36.w);
  static final v37 = SizedBox(height: Sizes.size37.w);
  static final v38 = SizedBox(height: Sizes.size38.w);
  static final v39 = SizedBox(height: Sizes.size39.w);
  static final v40 = SizedBox(height: Sizes.size40.w);
  static final v41 = SizedBox(height: Sizes.size41.w);
  static final v42 = SizedBox(height: Sizes.size42.w);
  static final v43 = SizedBox(height: Sizes.size43.w);
  static final v44 = SizedBox(height: Sizes.size44.w);
  static final v45 = SizedBox(height: Sizes.size45.w);
  static final v46 = SizedBox(height: Sizes.size46.w);
  static final v47 = SizedBox(height: Sizes.size47.w);
  static final v48 = SizedBox(height: Sizes.size48.w);
  static final v49 = SizedBox(height: Sizes.size49.w);
  static final v50 = SizedBox(height: Sizes.size50.w);
  static final v51 = SizedBox(height: Sizes.size51.w);
  static final v52 = SizedBox(height: Sizes.size52.w);
  static final v53 = SizedBox(height: Sizes.size53.w);
  static final v54 = SizedBox(height: Sizes.size54.w);
  static final v55 = SizedBox(height: Sizes.size55.w);
  static final v56 = SizedBox(height: Sizes.size56.w);
  static final v57 = SizedBox(height: Sizes.size57.w);
  static final v58 = SizedBox(height: Sizes.size58.w);
  static final v59 = SizedBox(height: Sizes.size59.w);
  static final v60 = SizedBox(height: Sizes.size60.w);
  static final v61 = SizedBox(height: Sizes.size61.w);
  static final v62 = SizedBox(height: Sizes.size62.w);
  static final v63 = SizedBox(height: Sizes.size63.w);
  static final v64 = SizedBox(height: Sizes.size64.w);
  static final v65 = SizedBox(height: Sizes.size65.w);
  static final v66 = SizedBox(height: Sizes.size66.w);
  static final v67 = SizedBox(height: Sizes.size67.w);
  static final v68 = SizedBox(height: Sizes.size68.w);
  static final v69 = SizedBox(height: Sizes.size69.w);
  static final v70 = SizedBox(height: Sizes.size70.w);
  static final v71 = SizedBox(height: Sizes.size71.w);
  static final v72 = SizedBox(height: Sizes.size72.w);
  static final v73 = SizedBox(height: Sizes.size73.w);
  static final v74 = SizedBox(height: Sizes.size74.w);
  static final v75 = SizedBox(height: Sizes.size75.w);
  static final v76 = SizedBox(height: Sizes.size76.w);
  static final v77 = SizedBox(height: Sizes.size77.w);
  static final v78 = SizedBox(height: Sizes.size78.w);
  static final v79 = SizedBox(height: Sizes.size79.w);
  static final v80 = SizedBox(height: Sizes.size80.w);
  static final v81 = SizedBox(height: Sizes.size81.w);
  static final v82 = SizedBox(height: Sizes.size82.w);
  static final v83 = SizedBox(height: Sizes.size83.w);
  static final v84 = SizedBox(height: Sizes.size84.w);
  static final v85 = SizedBox(height: Sizes.size85.w);
  static final v86 = SizedBox(height: Sizes.size86.w);
  static final v87 = SizedBox(height: Sizes.size87.w);
  static final v88 = SizedBox(height: Sizes.size88.w);
  static final v89 = SizedBox(height: Sizes.size89.w);
  static final v90 = SizedBox(height: Sizes.size90.w);
  static final v91 = SizedBox(height: Sizes.size91.w);
  static final v92 = SizedBox(height: Sizes.size92.w);
  static final v93 = SizedBox(height: Sizes.size93.w);
  static final v94 = SizedBox(height: Sizes.size94.w);
  static final v95 = SizedBox(height: Sizes.size95.w);
  static final v96 = SizedBox(height: Sizes.size96.w);
  static final v97 = SizedBox(height: Sizes.size97.w);
  static final v98 = SizedBox(height: Sizes.size98.w);
  static final v99 = SizedBox(height: Sizes.size99.w);
  static final v100 = SizedBox(height: Sizes.size100.w);

  // Horizontal Gaps
  static final h1 = SizedBox(width: Sizes.size1.h);
  static final h2 = SizedBox(width: Sizes.size2.h);
  static final h3 = SizedBox(width: Sizes.size3.h);
  static final h4 = SizedBox(width: Sizes.size4.h);
  static final h5 = SizedBox(width: Sizes.size5.h);
  static final h6 = SizedBox(width: Sizes.size6.h);
  static final h7 = SizedBox(width: Sizes.size7.h);
  static final h8 = SizedBox(width: Sizes.size8.h);
  static final h9 = SizedBox(width: Sizes.size9.h);
  static final h10 = SizedBox(width: Sizes.size10.h);
  static final h11 = SizedBox(width: Sizes.size11.h);
  static final h12 = SizedBox(width: Sizes.size12.h);
  static final h13 = SizedBox(width: Sizes.size13.h);
  static final h14 = SizedBox(width: Sizes.size14.h);
  static final h15 = SizedBox(width: Sizes.size15.h);
  static final h16 = SizedBox(width: Sizes.size16.h);
  static final h17 = SizedBox(width: Sizes.size17.h);
  static final h18 = SizedBox(width: Sizes.size18.h);
  static final h19 = SizedBox(width: Sizes.size19.h);
  static final h20 = SizedBox(width: Sizes.size20.h);
  static final h21 = SizedBox(width: Sizes.size21.h);
  static final h22 = SizedBox(width: Sizes.size22.h);
  static final h23 = SizedBox(width: Sizes.size23.h);
  static final h24 = SizedBox(width: Sizes.size24.h);
  static final h25 = SizedBox(width: Sizes.size25.h);
  static final h26 = SizedBox(width: Sizes.size26.h);
  static final h27 = SizedBox(width: Sizes.size27.h);
  static final h28 = SizedBox(width: Sizes.size28.h);
  static final h29 = SizedBox(width: Sizes.size29.h);
  static final h30 = SizedBox(width: Sizes.size30.h);
  static final h31 = SizedBox(width: Sizes.size31.h);
  static final h32 = SizedBox(width: Sizes.size32.h);
  static final h33 = SizedBox(width: Sizes.size33.h);
  static final h34 = SizedBox(width: Sizes.size34.h);
  static final h35 = SizedBox(width: Sizes.size35.h);
  static final h36 = SizedBox(width: Sizes.size36.h);
  static final h37 = SizedBox(width: Sizes.size37.h);
  static final h38 = SizedBox(width: Sizes.size38.h);
  static final h39 = SizedBox(width: Sizes.size39.h);
  static final h40 = SizedBox(width: Sizes.size40.h);
  static final h41 = SizedBox(width: Sizes.size41.h);
  static final h42 = SizedBox(width: Sizes.size42.h);
  static final h43 = SizedBox(width: Sizes.size43.h);
  static final h44 = SizedBox(width: Sizes.size44.h);
  static final h45 = SizedBox(width: Sizes.size45.h);
  static final h46 = SizedBox(width: Sizes.size46.h);
  static final h47 = SizedBox(width: Sizes.size47.h);
  static final h48 = SizedBox(width: Sizes.size48.h);
  static final h49 = SizedBox(width: Sizes.size49.h);
  static final h50 = SizedBox(width: Sizes.size50.h);
  static final h51 = SizedBox(width: Sizes.size51.h);
  static final h52 = SizedBox(width: Sizes.size52.h);
  static final h53 = SizedBox(width: Sizes.size53.h);
  static final h54 = SizedBox(width: Sizes.size54.h);
  static final h55 = SizedBox(width: Sizes.size55.h);
  static final h56 = SizedBox(width: Sizes.size56.h);
  static final h57 = SizedBox(width: Sizes.size57.h);
  static final h58 = SizedBox(width: Sizes.size58.h);
  static final h59 = SizedBox(width: Sizes.size59.h);
  static final h60 = SizedBox(width: Sizes.size60.h);
  static final h61 = SizedBox(width: Sizes.size61.h);
  static final h62 = SizedBox(width: Sizes.size62.h);
  static final h63 = SizedBox(width: Sizes.size63.h);
  static final h64 = SizedBox(width: Sizes.size64.h);
  static final h65 = SizedBox(width: Sizes.size65.h);
  static final h66 = SizedBox(width: Sizes.size66.h);
  static final h67 = SizedBox(width: Sizes.size67.h);
  static final h68 = SizedBox(width: Sizes.size68.h);
  static final h69 = SizedBox(width: Sizes.size69.h);
  static final h70 = SizedBox(width: Sizes.size70.h);
  static final h71 = SizedBox(width: Sizes.size71.h);
  static final h72 = SizedBox(width: Sizes.size72.h);
  static final h73 = SizedBox(width: Sizes.size73.h);
  static final h74 = SizedBox(width: Sizes.size74.h);
  static final h75 = SizedBox(width: Sizes.size75.h);
  static final h76 = SizedBox(width: Sizes.size76.h);
  static final h77 = SizedBox(width: Sizes.size77.h);
  static final h78 = SizedBox(width: Sizes.size78.h);
  static final h79 = SizedBox(width: Sizes.size79.h);
  static final h80 = SizedBox(width: Sizes.size80.h);
  static final h81 = SizedBox(width: Sizes.size81.h);
  static final h82 = SizedBox(width: Sizes.size82.h);
  static final h83 = SizedBox(width: Sizes.size83.h);
  static final h84 = SizedBox(width: Sizes.size84.h);
  static final h85 = SizedBox(width: Sizes.size85.h);
  static final h86 = SizedBox(width: Sizes.size86.h);
  static final h87 = SizedBox(width: Sizes.size87.h);
  static final h88 = SizedBox(width: Sizes.size88.h);
  static final h89 = SizedBox(width: Sizes.size89.h);
  static final h90 = SizedBox(width: Sizes.size90.h);
  static final h91 = SizedBox(width: Sizes.size91.h);
  static final h92 = SizedBox(width: Sizes.size92.h);
  static final h93 = SizedBox(width: Sizes.size93.h);
  static final h94 = SizedBox(width: Sizes.size94.h);
  static final h95 = SizedBox(width: Sizes.size95.h);
  static final h96 = SizedBox(width: Sizes.size96.h);
  static final h97 = SizedBox(width: Sizes.size97.h);
  static final h98 = SizedBox(width: Sizes.size98.h);
  static final h99 = SizedBox(width: Sizes.size99.h);
  static final h100 = SizedBox(width: Sizes.size100.h);
}
```

`font_size.dart`

```dart
import 'package:flutter_screenutil/flutter_screenutil.dart';

class FontSizes {
  static final size10 = 10.sp;
  static final size11 = 11.sp;
  static final size12 = 12.sp;
  static final size13 = 13.sp;
  static final size14 = 14.sp;
  static final size15 = 15.sp;
  static final size16 = 16.sp;
  static final size17 = 17.sp;
  static final size18 = 18.sp;
  static final size19 = 19.sp;
  static final size20 = 20.sp;
  static final size21 = 21.sp;
  static final size22 = 22.sp;
  static final size23 = 23.sp;
  static final size24 = 24.sp;
  static final size25 = 25.sp;
  static final size26 = 26.sp;
  static final size27 = 27.sp;
  static final size28 = 28.sp;
  static final size29 = 29.sp;
  static final size30 = 30.sp;
  static final size32 = 32.sp;
  static final size34 = 34.sp;
  static final size36 = 36.sp;
  static final size38 = 38.sp;
  static final size40 = 40.sp;
  static final size42 = 42.sp;
}
```



