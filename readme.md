# README.md



## 특화프로젝트 - 빅데이터를 이용한 와인 추천 서비스

### 사이트 주소
http://j6c102.p.ssafy.io/




### Backend 

|   분류    | 기술스택/라이브러리명 | 버전  | 비고 및 특이사항 |
| :-------: | :-------------------: | :---: | :--------------: |
|  Python   |        Python         | 3.9.6 |                  |
| Framework |        Django         | 3.2.9 |                  |
|           |                       |       |                  |
|           |                       |       |                  |

### devOp
지금 devOp는 태그가 정확히 되고 있지는 않음.(무조건 이미지가 푸쉬 되는식)
그러므로, 안전한 버전을 따로, 푸시해주시면, 좋을 듯 함.

docker 를 까시고,

docker login하시면 
아이디:ssafyc102
비밀번호 : 지메일과 비밀번호 동일. 

관련폴더 위치에서
```
docker build -t ssafyc102/wine_service:태그이름.버전 ./
docker push ssafyc102/wine_service:태그이름.버전
```

