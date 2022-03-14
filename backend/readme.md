## Backend 설정 및 실행



### 1. 가상환경 설정

```bash
#가상환경 생성
python -m venv venv

#가상환경 실행
source venv/Scripts/activate

#추가 모듈 설치 및 마이그레이션
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

#실행
python manage.py runserver
```

