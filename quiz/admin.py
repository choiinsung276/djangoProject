from django.contrib import admin
from  .models import Quiz
# Register your models here.
# 관리자 페이지에 퀴즈 모델을 등록하여 관리할수 있도록 처리
# 추가하고 python manage.py makemigrations
admin.site.register(Quiz)