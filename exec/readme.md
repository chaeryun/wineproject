## 소스 클론 이후 빌드 및 배포 가이드



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
- **Vuex 3.4.0**

**🖱CI/CD**

- **aws ec2**
- **docker**
- **nginx**
- **jenkins**



**DB : mongoDB**

**ID : ssafyC102**

**Password : ssafyC102**



## ⛑ 배포 시 특이사항

### 과정

- 아래 링크를 참고하여, 젠킨스를 원격 조종 시킵니다.

  ```
   https://velog.io/@king/Jenkins-Job-%EC%8B%A4%ED%96%89%EC%9D%84-%EC%9B%90%EA%B2%A9%EC%9C%BC%EB%A1%9C-%EC%9C%A0%EB%B0%9C%ED%95%98%EA%B8%B0-nuk5jjenyk
  ```



- 빌드는 최상단 파일/jenkinsFile 을 pipeline으로 읽게 만들어서, 진행합니다.



- 이 빌드가 성공적으로 마무리 되면,  젠킨스가 linux에 있는 deploy.sh를 실행합니다.

  (이때, freestyle 로만듬.)





### 특이사항

- 빌드 실패시, 딱히 알림이 오지는 않음.

- 빌드가 이상하다고 생각하면, jenkins를 살펴보시면 됩니다. 

  -  아이디: ssafyc102
  -  비밀번호: C102ssafy!

- 로그를 보고, 이상한점을 유추하시면됩니다.

- 처음 배포할 때는 linux에 최상단에 있는 docker-compose.yml와 deploy.sh를 복붙해줍니다.

  - docker-compose 아래 명령어로 수행합니다.

  ```
  docker-compose up -d
  ```

- 설치해야할 것은 docker, docker-compose 정도 있습니다.

-  해당 이미지 허브는 ssafyc102/wine_service입니다.

  - 안되시면 로그인 해보세요.


  - 젠킨스 아이디,비밀번호 동일함.
