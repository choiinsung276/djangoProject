# rest api study 

참고 - https://www.youtube.com/watch?v=ywJWbAF6txQ

# DJango api

* 프로젝트 만들기
* django-admin startproject 프로젝트명 .
* 앱 만들기
* python [manage.py](http://manage.py)startapp 앱명
* 프로젝트 [settings.py](http://settings.py)에 allowed\_hosts 에 전체 연결
* 시간설정 , 정적파일 경로 설정

``` python
# settings.py
TIME_ZONE = 'Asia/Seoul'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'rest_framework',
]
```

* 마이그레이션 및 마이그레이트

```
python manage.py makemigrations
python manage.py migrate
```

* 시리얼라이즈는 장고 모델 데이터를 json 타입으로 바꿔주는 코드
* [view.py](http://view.py)에서 api코드 작성
* 앱url과 프로젝트 url 연결해주기
* api 만들고 모델을 관리자에 등록
* python [manage.py](http://manage.py)createsuperuser 로 관리자 생성

- - -
