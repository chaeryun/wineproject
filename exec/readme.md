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

- Frontend 빌드 가이드

- Backend 빌드 가이드

  - ```bash
    cd backend 백엔드 디렉토리 이동
    python -m venv venv 가상환경 생성 
    source venv/Scripts/Activate 가상환경 실행
    
    pip install -r requirements.txt 의존성 library 설치
    python manage.py makemigrations 마이그레이션 생성
    python manage.py migrate 마이그레이션 실행
    
    python manage.py runserver 백엔드 환경 실행
    ```

- 기타 특이사항
