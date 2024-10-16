[강의](https://www.youtube.com/watch?v=Y__GznCpioo&list=PLEOnZ6GeucBWaUzqrMvrl-_ernhNwLHOr)

was: 서버가 애플리케이션 역할까지 같이 수행

ws: 

서버를 구성할때 nginx를 둠 (80)

사용자는 https://domain.com -> nginx

사용자의 요청을 ws가 먼저 받음

nginx는 node 서버를 띄움 (9001)

flask도 띄웠다고보면 (9002)

nginx는 80포트의 index.html을 서비스함

사용자의 모니터에는 index.html이 나옴

url을 /api/users 같이 호출

도메인 다음 기준이 되는 정보를 name space

네임스페이스에 따라서 node로 갈 것인지 flask로 갈 것인지 구성할 수 있음

프록시는 한쪽에서 다른 쪽으로 보내는 것, 통로역할

방화벽은 nginx 앞단에 있음

