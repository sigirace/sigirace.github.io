### ✏️ DOM

**DOM(Document Object Model)**은 웹 페이지의 HTML 또는 XML 문서를 **객체 모델**로 표현한 것입니다. DOM을 통해 JavaScript와 같은 프로그래밍 언어로 웹 페이지를 동적으로 제어하고, 페이지 구조를 탐색하거나 수정할 수 있습니다.

### 1. **DOM의 기본 개념**

   - DOM은 웹 페이지를 계층적 구조로 표현하며, 페이지의 각 요소를 **객체**로 나타냅니다.
   - 이 구조는 **트리(tree) 구조**로 이루어져 있으며, HTML 문서의 각 요소(`<html>`, `<body>`, `<div>`, `<p>` 등)가 **노드(node)**로 표현됩니다.
   - DOM을 사용하면 JavaScript가 문서의 구조, 스타일 및 콘텐츠를 동적으로 조작할 수 있습니다.

### 2. **DOM 트리 구조**

   - **루트 노드**: DOM 트리의 최상위 노드는 `<html>` 태그이며, 루트 노드라고도 합니다.
   - **부모와 자식 관계**: DOM 트리에서 각 요소는 부모와 자식 관계를 형성합니다. 예를 들어, `<body>`는 `<html>`의 자식이며, `<div>`는 `<body>`의 자식입니다.
   - **형제 노드**: 동일한 부모 아래 있는 노드들을 형제 노드(sibling nodes)라고 합니다.
   - **노드 타입**: DOM에서 각 노드는 다음과 같은 여러 타입으로 나뉩니다.
     - **요소 노드(Element Node)**: HTML 태그를 나타냅니다. 예: `<div>`, `<p>`.
     - **텍스트 노드(Text Node)**: HTML 요소 내의 텍스트 콘텐츠를 나타냅니다.
     - **속성 노드(Attribute Node)**: HTML 요소의 속성을 나타냅니다. 예: `id`, `class`.
     - **주석 노드(Comment Node)**: HTML 문서 내 주석을 나타냅니다. 예: `<!-- 주석 내용 -->`.

### 3. **DOM의 주요 객체와 메서드**

   - **`document` 객체**: 웹 페이지의 루트 객체로, DOM 트리에 접근하기 위한 시작점입니다.
     - 예: `document.getElementById('container')`는 `id`가 `container`인 요소에 접근합니다.
   - **DOM 탐색 메서드**:
     - **`getElementById()`**: 특정 `id`를 가진 요소를 찾습니다.
     - **`getElementsByClassName()`**: 특정 클래스를 가진 모든 요소를 찾습니다.
     - **`getElementsByTagName()`**: 특정 태그 이름을 가진 모든 요소를 찾습니다.
     - **`querySelector()`**: CSS 선택자를 사용하여 처음 일치하는 요소를 찾습니다.
     - **`querySelectorAll()`**: CSS 선택자를 사용하여 일치하는 모든 요소를 찾습니다.
   - **DOM 조작 메서드**:
     - **`createElement()`**: 새로운 요소를 생성합니다.
     - **`appendChild()`**: 새로운 요소를 부모 노드의 마지막 자식으로 추가합니다.
     - **`removeChild()`**: 특정 자식 요소를 제거합니다.
     - **`setAttribute()`**: 요소에 속성을 추가하거나 변경합니다.
     - **`innerHTML`**: 요소의 HTML 콘텐츠를 설정하거나 반환합니다.
     - **`textContent`**: 요소의 텍스트 콘텐츠를 설정하거나 반환합니다.

   예시:

   ```javascript
const container = document.getElementById('container');
const newParagraph = document.createElement('p');
newParagraph.textContent = 'New Paragraph';
container.appendChild(newParagraph);
   ```

### 4. **DOM을 사용한 동적 웹 페이지 구성**

   - JavaScript와 DOM을 사용하면 웹 페이지의 내용을 사용자의 상호작용에 따라 **실시간으로 업데이트**할 수 있습니다.
   - 예를 들어, 버튼 클릭 시 새로운 요소를 추가하거나, 사용자 입력에 따라 특정 요소의 스타일을 변경할 수 있습니다.
   - 이러한 동적 페이지 구성은 웹 애플리케이션이 사용자 경험을 크게 개선하는 데 도움이 됩니다.

### 5. **DOM 이벤트 처리**

   - DOM은 사용자와의 상호작용(예: 클릭, 키보드 입력 등)을 처리하는 **이벤트 시스템**을 제공합니다.

   - JavaScript로 이벤트 리스너를 추가하여, 특정 이벤트 발생 시 수행할 동작을 정의할 수 있습니다.

   - 예:

     ```javascript
     const button = document.getElementById('myButton');
     button.addEventListener('click', function() {
       alert('Button clicked!');
     });
     ```

### 6. **DOM의 중요성 및 활용**

   - DOM은 JavaScript와 같은 언어를 통해 **정적 웹 페이지를 동적 웹 애플리케이션**으로 전환하는 데 필수적인 역할을 합니다.
   - DOM을 사용하여 웹 페이지의 콘텐츠를 실시간으로 업데이트하거나, 사용자 입력에 따라 반응하는 기능을 구현할 수 있습니다.
   - 이를 통해 웹 페이지의 인터랙티브성을 높이고, 보다 사용자 친화적인 애플리케이션을 만들 수 있습니다.

### 7. **DOM의 제한사항**

   - DOM은 트리 구조이므로, 매우 큰 DOM 트리는 **성능에 영향을 미칠 수 있습니다.** 예를 들어, 노드가 많을수록 탐색 및 조작이 느려질 수 있습니다.
   - 브라우저 간 DOM 구현 방식이 다를 수 있어, 특정 DOM 조작이 **브라우저 호환성** 문제를 야기할 수 있습니다.

DOM은 웹 페이지와 사용자 간의 상호작용을 가능하게 하고, 동적 콘텐츠 구성을 통해 다양한 웹 애플리케이션을 구현할 수 있는 중요한 기술입니다.