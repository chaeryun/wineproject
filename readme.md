# 🍷와인어때 (빅데이터를 이용한 와인 추천 서비스)



## 💎와인어때 소개 및 시연 영상💎

### Service URL : http://j6c102.p.ssafy.io/

### [영상 링크]



## ✨Overview

#### 와인을 알고 싶지만 멀게만 느껴지는 당신! 당신에게 딱 맞는 와인을 추천해드리기 위해 "와인어때"서비스가 왔습니다!



## 👁 서비스 화면

[캡쳐사진]

## ✨ 핵심 기능 및 특장점

- 주요 기능 :
  - 1
  - 2
  - 3

### 🖥️ 개발 환경

------

🖱**Backend**

- **Django REST Framework 3.13.1 & Django 3.2.9**
- **pandas library 1.4.1**
- **Python 3.9.6**
- **MongoDB**
- **AWS EC2**

**🖱Frontend**

- **Visual Studio Code**
- **Vue 2.6.11**
- **Vuetify 2.6.0**

**🖱CI/CD**

- **aws ec2**

- **docker**

- **nginx**

- **jenkins**

  

## 🚀 서비스 아키텍쳐

[아키텍쳐 그림 그려서 올리기]











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

