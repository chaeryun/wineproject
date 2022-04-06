FROM python:3
WORKDIR /usr/src/app
# requirements.txt에 명시된 필요한 packages 설치
COPY requirements.txt ./
COPY manage.py ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U drf-yasg

RUN python manage.py makemigrations
RUN python manage.py migrate


# Project를 /usr/src/app으로 복사
COPY . .
# 포트 설정
EXPOSE 8000
# gunicorn 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
