
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView

# http://localhost:8000 요청이 들어왔을때 전체 project의 홈페이지로 이동
# Django 는 elegant URL을 지원
# 정규표현식 (regular expression )
# 시작 => ^, 끝 => $
# [0-9] : 1글자를 지칭
# {3} : 3번 반복을 지칭
# [0-9]{4} : 4자리 숫자
# r(raw)은 escape 문자를 한번 더 사용하지 않도록 처리. \ 한번만 사용
# r"^[0-9]{1,3}$" : 1 or 2 or 3 자리 숫자중 하나
# r"^010[1-9]\d{6,7}$" : 전화번호

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name='index.html'), name="home"),
    path('admin/', admin.site.urls),
    path('my_bbs/', include('my_bbs.urls'))

]
